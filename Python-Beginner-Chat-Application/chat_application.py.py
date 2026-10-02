print("Simple Chat Application")
print("Type 'bye' to exit.\n")

while True:
    user_message = input("You: ")

    if user_message.lower() == "hello":
        print("Bot: Hello! How are you?")
    elif user_message.lower() == "how are you":
        print("Bot: I'm fine, thank you!")
    elif user_message.lower() == "what is your name":
        print("Bot: I'm your Python Chat Bot.")
    elif user_message.lower() == "bye":
        print("Bot: Goodbye!")
        break
    else:
        print("Bot: Sorry, I don't understand that.")
