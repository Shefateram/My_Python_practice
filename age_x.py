def is_adult(x):
    if x >= 18:
        return True
    else:
        return False

age = int(input("What's your age? "))

if is_adult(age):
    print("You can Vote!")
else:
    print("You cannot Vote!")
  
