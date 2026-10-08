count = 5
total = 0

for n in range(count):
    x = int(input("Type 5 nos to add: "))
    total = total + x

print(f"Total sum: {total}")
avg = total / count
print(f"Avg: {avg}")
