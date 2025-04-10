# Sample Chatbot with Chainlit

This is a simple chatbot application built using the Chainlit framework. The chatbot demonstrates basic functionality of receiving user messages and responding to them.

## Features

- Real-time chat interface
- Echo functionality (responds with what the user said)
- Asynchronous message handling

## Technologies Used

- Python
- Chainlit - A framework for building chat applications

## Installation

1. Clone this repository
2. Install the required dependencies:

```bash
pip install chainlit
```

## Usage

To run the chatbot:

```bash
chainlit run main.py
```

This will start a local server and open a browser window with the chat interface. You can type messages in the input field and the chatbot will respond by echoing back what you said.

## How It Works

The chatbot uses Chainlit's `@cl.on_message` decorator to listen for incoming messages. When a user sends a message, the `main` function is triggered asynchronously. The function creates a response by prefixing the user's message with "You said:" and sends it back to the user.

## Project Structure

- `main.py` - Contains the chatbot logic
- `README.md` - Project documentation

## Extending the Chatbot

This is a basic implementation that can be extended with:

- More sophisticated response logic
- Integration with AI models
- Custom UI elements
- Persistent conversation history
- User authentication

## License

This project is open source and available under the MIT License.
