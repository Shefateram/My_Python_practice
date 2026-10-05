def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False

number = int(input("What's x? "))
result = is_even(number)

if result:
    print(f"{number} is even")
else:
    print(f"{number} is odd")
