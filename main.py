import os, sys

from taipy.gui import Gui, State, notify
import openai

client = None
context = "The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today? "
conversation = {"Discussion": []}
current_user_message = ""


def request(state: State, prompt: str) -> str:
    """
    Send a prompt to the GPT-3 API and return the response.

    Args:
        - state: The current state of the app.
        - prompt: The prompt to send to the API.

    Returns:
        The response from the API.
    """
    response = state.client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"{prompt}",
            }
        ],
        model="gpt-3.5-turbo",
    )
    return response.choices[0].message.content


def update_context(state: State) -> None:
    """
    Update the context with the user's message and the AI's response.

    Args:
        - state: The current state of the app.
    """
    state.context += f"Human: \n {state.current_user_message}\n\n AI:"
    answer = request(state, state.context).replace("\n", "")
    state.context += answer
    return answer


def send_message(state: State) -> None:
    """
    Send the user's message to the API and update the context.

    Args:
        - state: The current state of the app.
    """
    notify(state, "info", "Sending message...")
    answer = update_context(state)
    conv = state.conversation._dict.copy()
    conv["Discussion"] += [state.current_user_message, answer]
    state.current_user_message = ""
    state.conversation = conv
    notify(state, "success", "Response received!")


def style_conv(state: State, idx: int, row: int) -> str:
    """
    Apply a style to the conversation table depending on the message's author.

    Args:
        - state: The current state of the app.
        - idx: The index of the message in the table.
        - row: The row of the message in the table.

    Returns:
        The style to apply to the message.
    """
    if idx is None:
        return None
    elif idx % 2 == 0:
        return "user_message"
    else:
        return "gpt_message"


def on_exception(state, function_name: str, ex: Exception) -> None:
    """
    Catches exceptions and notifies user in Taipy GUI

    Args:
        state (State): Taipy GUI state
        function_name (str): Name of function where exception occured
        ex (Exception): Exception
    """
    notify(state, "error", f"An error occured in {function_name}: {ex}")


page = """
<br/>
<|{conversation}|table|style=style_conv|show_all|width=100%|>
<br/>

<|{current_user_message}|input|label=Write your message here...|on_action=send_message|class_name=fullwidth|multiline|>
"""

if __name__ == "__main__":
    if os.getenv("OPENAI_API_KEY"):
        api_key = os.getenv("OPENAI_API_KEY")
    elif len(sys.argv) > 1:
        api_key = sys.argv[1]
    else:
        raise ValueError(
            "Please provide the OpenAI API key as an environment variable OPENAI_API_KEY or as a command line argument."
        )

    client = openai.Client(api_key=api_key)

    Gui(page).run(debug=True)
