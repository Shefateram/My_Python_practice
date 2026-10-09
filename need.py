items = { "mango": 100,
"pineapple": 70,
"banana": 120,
}
need = input("What item do you need? ")
if need in items:
    print(f"{need}: {items[need]}")
else:
    print("Sorry, we dont have it!")
