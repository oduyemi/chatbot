# ChatBot

## Overview

ChatBot is a simple Python project that utilizes the OpenAI API to create a conversational chatbot powered by the GPT-3.5 model. This chatbot can engage in text-based conversations with users by generating responses based on the input provided by the user.

## Installation

1. Clone the repository to your local machine:

    ```
    git clone https://github.com/oduyemi/chatbot.git
    ```

2. Navigate to the project directory:

    ```
    cd chatbot
    ```

3. Install the required dependencies:

    ```
    pip install -r requirements.txt
    ```

## Configuration

1. Obtain an API key from OpenAI. You can sign up for an account and get your API key from the OpenAI website.

2. Set up your API key as an environment variable. You can either export it in your shell or create a `.env` file in the project directory and store the API key there:

    ```
    API_KEY=api-key from OpenAI
    ```

## Usage

1. Run the main script `main.py`:

    ```
    python main.py
    ```

2. Enter your message when prompted by the chatbot:

    ```
    You: Hello, how are you today?
    ```

3. The chatbot will generate a response based on your input and display it:

    ```
    ChatBot: [Generated Response]
    ```

4. Continue the conversation by entering more messages. To exit the chat, type "quit", "exit", or "bye".

## Project Structure

The project structure is as follows:

- `main.py`: The main script to run the chatbot.
- `instance/config.py`: Configuration file containing constants and settings (e.g., API key).
- `requirements.txt`: File containing a list of required Python packages.

## Dependencies

- `openai`: Python package for interacting with the OpenAI API.
- `dotenv`: Python package for loading environment variables from a .env file.

## License

This project is licensed under the [MIT License](LICENSE).

## Credits

- Developed by me (Opeyemi Oduyemi(https://github.com/oduyemi)).

## Feedback and Contributions

Feedback, bug reports, and contributions are welcome! Please feel free to submit issues or pull requests on GitHub.
