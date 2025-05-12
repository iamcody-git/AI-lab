print("You can interact with the system with the following statements:\n -> hi / hello \n -> how are you? \n -> what did you do yesterday? \n -> exit")

while True:
    statement = input("Enter a statement: ")
    statement = statement.lower()

    if statement in ["hi", "hello"]:
        print("What's up?")
    elif statement == "how are you?":
        print("Doing good.")
    elif statement == "what did you do yesterday?":
        print("I wrestled.")
    elif statement == "exit":
        print("Good day.")
        break
    else:
        print("I don't understand that statement.")
