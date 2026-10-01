#ask the student for there score
score = int(input("score: "))

if score >= 85 and score <= 100:
    print("Grade: A")
elif score >= 75 and score < 85:
    print("Grade: B")
elif score >= 60 and score < 75:
    print("Grade: C")
elif score >= 40 and score < 60:
    peint("Grade: D")
else:
    print("Grade: F")
