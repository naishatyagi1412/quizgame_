score = 0

print("Welcome to the Quiz Game!\n")

# Question 1
answer = input("What is the capital of France? ")
if answer.lower() == "paris":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

# Question 2
answer = input("Which language is used for Python programs? ")
if answer.lower() == "python":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

# Question 3
answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

print(f"\nYour final score is: {score}/3")
print("thanks for playing!")