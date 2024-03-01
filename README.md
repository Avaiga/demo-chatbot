# Taipy LLM Chat Demo

<p align="center">
  <img src="media/round_conv.png" alt="A conversation about calibers" width="100%"/>
</p>

A simple app to chat with an LLM which can be used to create any LLM Inference Web Apps using Python only.

This particular app uses OpenAI's GPT-3 API to generate responses to your messages. You can easily change the code to use any other API or model.

## Tutorial

A tutorial on how to create this app is available in the <a href="https://docs.taipy.io/en/release-3.0/knowledge_base/tutorials/chatbot/" target="_blank">Taipy documentation</a>

## How to Use

**You need an OpenAI account with an active <a href="https://platform.openai.com/api-keys" target="_blank">API key</a>**

1. Clone this repo:

```bash	
git clone https://github.com/Avaiga/demo-llm-chat.git
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the app using your API key as an argument:

```bash
python main.py sk-XXXXX...XXXXX
```

(You can also set the `OPENAI_API_KEY` environment variable instead of passing it as an argument)