# AI-Chatbot-Web-Interface

This task is a web-based chatbot interface that uses Google's Generative AI to interact with users while maintaining the context of the conversation. The task consists of a Python backend using the Flask framework and a frontend using HTML, CSS, and JavaScript. The chatbot accepts user inputs through a web interface, sends these inputs along with the conversation history to the AI model for generating responses, and then displays the responses back on the web page.

## File Descriptions

### `app.py`
- This is the main backend file for the project.
- It sets up the Flask web server.
- Configures the Google Generative AI API with the provided API key.
- Uses Flask-Session to store the conversation history in the session.
- Defines two routes:
  - `/` for serving the homepage and initializing an empty conversation.
  - `/chat` for handling chat messages sent by the user and maintaining the conversation context.
- Processes the user's message, appends it to the conversation history, generates a response using the AI model, and stores the updated conversation history back in the session.

### `templates/index.html`
- This is the main HTML file that defines the structure of the web page.
- Contains a simple chat interface with a message display area and an input field for the user to type messages.
- Includes CSS for styling the chat interface.
- Contains JavaScript to handle user interactions, send messages to the backend, and update the chat interface with responses from the AI model.
