# Taipy LLM Chat Demo

<p align="center">
  <img src="media/round_conv.png" alt="A conversation about calibers" width="100%"/>
</p>

A simple app to chat with an LLM which can be used to create any LLM Inference Web Apps using Python only.

This particular app uses OpenAI's GPT-4 API to generate responses to your messages. You can easily change the code to use any other API or model.

## Tutorial

A tutorial on how to create this app is available in the <a href="https://docs.taipy.io/en/release-3.0/knowledge_base/tutorials/chatbot/" target="_blank">Taipy documentation</a>

<p align="center">
  <img src="media/docs.png" alt="LLM Chatbot Tutorial" width="80%"/>
</p>


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

3. Create a `.env` file in the root directory with the following content:

```bash
OPENAI_API_KEY=sk-...
```

4. Run the app:

```bash
python main.py
```