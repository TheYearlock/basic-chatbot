# Add more and more examples to make your experience better.

import nltk
nltk.download('punkt') # Download the necessary data for NLTK
from nltk.chat.util import Chat, reflections

# Define the responses for the bot
pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey!"]
    ],
    [
        r"what is your name?",
        ["My name is ChatBot.", "People call me ChatBot."]
    ],
    [
        r"how are you?",
        ["I'm doing fine, thank you.", "I'm good. How can I help you?"]
    ],
    [
        r"quit",
        ["Bye! Take care.", "Goodbye!"]
    ],
    [
        r".*",
        ["Sorry, I did not understand. Could you please repeat that?", "I'm not sure I understand."]
    ]
]

# Create the chat bot
chatbot = Chat(pairs, reflections)

# Start the conversation loop
print("Hi! I'm ChatBot. How can I help you today?")
while True:
    try:
        user_input = input("> ")
        response = chatbot.respond(user_input)
        print(response)
    except (KeyboardInterrupt, EOFError):
        break
