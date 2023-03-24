from __future__ import annotations

import datetime
import webbrowser
from typing import Any, List, Mapping, Optional

import openai
from langchain.agents import Tool, tool
from langchain.chains import LLMChain, SimpleSequentialChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.prompts.chat import ChatPromptTemplate, HumanMessagePromptTemplate


@tool(return_direct=True)
def picture(query: str) -> str:
    """Generates a picture, or an image of whatever the user asks for."""
    image_resp = openai.Image.create(prompt=query, n=1, size="512x512")
    return f"{image_resp.data[0].url}"

@tool
def get_time(query: str) -> str:
    """Returns the current time in the isoformat standard time format."""
    return datetime.datetime.now().isoformat(sep=" ")

class PictureChain(LLMChain):
    """Calls the picture tool and returns the answer directly."""
    # input_chain: LLMChain
    picture: Tool
    n: int
    size: str

    @property
    def input_keys(self) -> List[str]:
        # SimpleSequentialChains require this to have one input.
        # We integrate the image model params as instance variables at instantiation time.
        return ["query"]

    @property
    def output_keys(self) -> List[str]:
        # SimpleSequentialChains require this to have one input.
        return ['picture_output']

    def _call(self, inputs: Dict[str]) -> Dict[str]:
        output_1 = self.picture.run(inputs['query'], self.n, self.size)
        return {'picture_output': output_1}

class TimeChain(LLMChain):
    """Re-implements human-readable times using LLMs, similar to the pendulum library."""
    get_time: Tool

    @property
    def output_keys(self) -> List[str]:
        # SimpleSequentialChains require this to have one input.
        return ['dalle-description']

    @property
    def input_keys(self) -> List[str]:
        return ['time_and_location']

    def _call(self, inputs: Dict[str]) -> Dict[str]:
        desc = LLMChain._call(self, inputs)
        return {'dalle-description': desc['text']}

human_asks_dumb_question_about_shadows_prompt = HumanMessagePromptTemplate(
        prompt=PromptTemplate(
            template="Suggest whether the sun at {time_and_location} might be likely to be high in the sky or low in the sky? What might the shadows in this location be like? Ensure your answer starts with 'Here in {time_and_location},'",
            input_variables=["time_and_location"],
        )
)

shadows_prompt_template = ChatPromptTemplate.from_messages([human_asks_dumb_question_about_shadows_prompt])
chat = ChatOpenAI(temperature=0.9)
chain_zero = TimeChain(get_time=get_time, llm=chat, prompt=shadows_prompt_template, verbose=True)

human_message_prompt = HumanMessagePromptTemplate(
        prompt=PromptTemplate(
            template="Write a down-to-earth and realistic Dall-e prompt describing an oil painting of a historic and traditional landmark from the following location and lighting description: \
            {dalle-description}. Be sure to choose a specific famous painter from this country and geographic region for the art style.",
            input_variables=["dalle-description"],
        )
    )
chat_prompt_template = ChatPromptTemplate.from_messages([human_message_prompt])
chat = ChatOpenAI(temperature=0.9)
chain = LLMChain(llm=chat, prompt=chat_prompt_template)
print(chain.run("Limerick"))

second_prompt = PromptTemplate(
    input_variables=["picture_prompt"],
    template="{picture_prompt}",
)
chain_two = PictureChain(picture=picture, llm=chat, prompt=second_prompt, n=1, size="512x512")

overall_chain = SimpleSequentialChain(chains=[chain_zero, chain, chain_two], verbose=True)

# Run the chain specifying only the input variable for the first chain.
lim_pic = overall_chain.run("Limerick, Ireland " + "at " + get_time.run(None))
webbrowser.open_new_tab(lim_pic)
