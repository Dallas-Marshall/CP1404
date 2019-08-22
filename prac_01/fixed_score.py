MIN_SCORE = 0
MAX_SCORE = 100

score = float(input("Enter score: "))

if score < MIN_SCORE or score > MAX_SCORE:
    print("Invalid Score!")
elif score >= 90:
    print("Excellent score!")
elif score >= 50:
    print("Passable score!")
else:
    print("Bad Score!")
