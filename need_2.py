items = { 
          "mango": 100,
          "pineapple": 70,
          "banana": 120,
        }
need = input("What item do you need? ")

if need in items:
    how_many = int(input("How many do you need? "))
    print(f"{need}: {items[need]}")
    total = items[need] * how_many
    print(f"Total: {total}rs")
else:
    print("Sorry, we dont have it!")
