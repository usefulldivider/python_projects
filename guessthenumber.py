import random
print("Welcome to the number guessing game\n I am thinking of a number between 1 and 100 guess the number ")
difficulty=input("Enter your difficulty : easy or hard\n").lower()
if difficulty=="hard":
    attempt=5
elif difficulty=="easy":
    attempt=10
else:
    print("Invalid")
    exit()
done =False
print(f"You chose {difficulty} so you have {attempt}attempts")
cnum=random.randint(1,100)
while attempt!=0 and not done:
    gnum=int(input("Enter your guess"))
    if gnum==cnum:
        print("You got it!")
        done=True
    elif gnum>cnum:
        print("guess is too high")
        attempt-=1
        print(f"You have {attempt} attempts left")
    elif gnum<cnum:
        print("guess is too low")
        attempt-=1
        print(f"You have {attempt} attempts left")

if attempt==0:
    print(f"You have exhausted your tries \nThe number was {cnum}")