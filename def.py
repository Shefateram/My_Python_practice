def is_even(x):
    return x % 2 == 0

number = int(input("What's x? "))


if is_even(number):
    print(f"{number} is even")
else:
    print(f"{number} is odd")
