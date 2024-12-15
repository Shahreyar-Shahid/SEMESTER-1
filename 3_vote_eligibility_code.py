print("Vote Eligibility Booth")

name = input("What is your name? ")
print(f"Hello, {name}! Welcome to the voting booth.")

age = int(input("What is your age? "))

if age >= 18:
    print("You are eligible to vote in the UK.")
else:
    print("You are not eligible to vote in the UK yet.")
