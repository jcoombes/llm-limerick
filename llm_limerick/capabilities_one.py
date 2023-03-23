from __future__ import annotations

import webbrowser

import openai

# list models
models = openai.Model.list()

# print the first model's id
print(models.data[0].id)

# create a completion
# completion = openai.Completion.create(model="ada", prompt="Hello world")
# chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world!, can you write me a poem about waking up?"}])
image_resp = openai.Image.create(prompt="two dogs playing chess, oil painting", n=1, size="512x512")



# print the completion
# print(completion.choices[0].text)
# print(chat.choices[0].message.content)
print(webbrowser.open_new_tab(image_resp.data[0].url))