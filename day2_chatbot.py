name = input("Enter your name: ")

replies = {
    "hello": "Hi! How are you?",
    "hi": "Hello! Welcome!",
    "python": "Python is easy to learn!",
    "bye": "Goodbye!"
}

history = []

while True:
    message = input(name + ": ").lower().strip()

    history.append({"role": "user", "content": message})

    if message == "bye":
        print("Bot:", replies["bye"])
        break

    if message in replies:
        answer = replies[message]
    else:
        answer = "Sorry, I don't understand."

    print("Bot:", answer)

    history.append({"role": "bot", "content": answer})

print("Conversation History:")
print(history)