name = input("What is your name? ")
age = int(input("What is your age? "))
year = int(input("Type year: "))

age_30 = 30 - age
turn_30 = year + age_30

print(f"Ms/Mr {name}, right now as of {year} you are {age} and will turn 30 year old in year {turn_30}")
