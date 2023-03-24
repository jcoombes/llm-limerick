from __future__ import annotations

from langchain.agents import initialize_agent, load_tools
from langchain.llms import OpenAI

llm = OpenAI(temperature=0)

tools = load_tools(["wikipedia", "python_repl"], llm=llm)

agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)

agent.run("Where is the centre of the old kingdom of Thomond and what is the age of the kingdom raised to the 0.43 power?")