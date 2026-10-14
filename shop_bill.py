items = {
    "chocolate": 50,
    "lays": 20,
    "chewing gum": 30, #spelling might be incorrect
    "kurkure": 20,
    "kitkat": 100,
    "oreo": 20,
    "kinder joy": 50,
    "coffee pack": 10,
    "bladelets": 200,
    "ramen": 50,
}

total = 0

while True:
    need = input("What do you need? ").lower()
    if need =="done":
        break

    if need in items:
        print(f"{need}: {items[need]}")
        how_many = int(input("How much do you need? "))
        total = total + items[need] * how_many
        print(f"Total: {total}rs")
    else:
        print("Sorry! We dont have it")

print(f"Total bill: {total}rs")
