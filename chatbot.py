print("================================")
print("        PYTHON CHATBOT")
print("================================")
print("Type 'bye' to exit the chatbot.")

while True:

    user_input = input("\nYou: ").lower()

    if user_input == "hello" or user_input == "hi":
        print("Bot: Hello! How can I help you?")

    elif user_input == "how are you":
        print("Bot: I'm doing great! Thanks for asking.")

    elif user_input == "what is your name":
        print("Bot: I am a simple Python chatbot.")

    elif user_input == "help":
        print("Bot: You can say hello, ask how I am, ask my name, or say bye.")

    elif user_input == "bye":
        print("Bot: Goodbye! Have a great day!")
        break

    else:
        print("Bot: Sorry, I don't understand that.")