# llm-limerick

[![CI](https://github.com/jcoombes/llm-limerick/actions/workflows/main.yaml/badge.svg)](https://github.com/jcoombes/llm-limerick/actions/workflows/main.yaml)

Conference talk about language models

https://python.ie/

PyCon Limerick 2023-03-24 Wogan Sat 3:50 - 4:30

LangChain, GPT-3 and Me: Exploring the Promises and Perils of Large Language Models
Large language models like Open AI's ChatGPT, Google's Bard and Meta's Llama have generated excitement and controversy beyond the AI community. These models are trained on massive amounts of text data, and can generate human-like responses to a wide variety of language tasks. How can we, as Pythonistas, use them to create tools?

We'll start by introducing the basics of language models and how we can use them today. We'll briefly discuss the history of language models. We skim over their evolution from rule-based systems to state-of-the-art deep learning models. We'll discuss the promises of this new technology and address the perils associated with language models. These include bias, AI alignment and misinformation.

Then, we'll introduce the LangChain library. It allows users to build and combine language models in a modular way. We will discuss the abstractions used by this library. Next, a small project demonstrates the library's power and versatility.

This talk shows potential benefits and ethical challenges of large language models. This talk will equip with some practical tools for exploring this exciting technology.

## Project cheatsheet

- **pre-commit:** `pre-commit run --all-files`
- **pytest:** `pytest` or `pytest -s`
- **coverage:** `coverage run -m pytest` or `coverage html`
- **poetry sync:** `poetry install --no-root --sync`
- **updating requirements:** see [docs/updating_requirements.md](docs/updating_requirements.md)

## Initial project setup

1. See [docs/getting_started.md](docs/getting_started.md) or [docs/quickstart.md](docs/quickstart.md)
   for how to get up & running.
2. Check [docs/project_specific_setup.md](docs/project_specific_setup.md) for project specific setup.
3. See [docs/using_poetry.md](docs/using_poetry.md) for how to update Python requirements using
   [Poetry](https://python-poetry.org/).
4. See [docs/detect_secrets.md](docs/detect_secrets.md) for more on creating a `.secrets.baseline`
   file using [detect-secrets](https://github.com/Yelp/detect-secrets).
