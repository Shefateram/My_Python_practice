#using match fuction

name = input("What is your name? ")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Grifindor")
    case "draco":
        print("Slytherin")
    case _:
        print("Who?")
