import json

with open("responses.json") as file:
    data = json.load(file)

print("AI Chatbot (type 'exit' to quit)")

while True:
    user = input("You: ").lower()

    if user in data["greetings"]:
        print("Bot:", data["responses"]["greetings"])

    elif "name" in user:
        print("Bot:", data["responses"]["name"])

    elif user == "exit":
        print("Bot:", data["responses"]["bye"])
        break

    else:
        print("Bot: Sorry, I didn't understand that.")