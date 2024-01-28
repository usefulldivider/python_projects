from necessities import art,data
import random
points=0
print(f"Welcome to\n{art[0]}\nGoal of the game : two instagram personalities will be shown you have to guess which one has the higher follower count \nThe more you guess correct, the more points you will get\nGoodluck")
print("press 1  for the first option and 2 for the second")


i1=random.randint(0,len(data)-1)
op1=data.pop(i1)

game_over=False

while not game_over:
    if points >= 48:
        print(f"You have reached maxixum amount of  points attainable of {points} !!!")
        exit()
    i2=random.randint(0,len(data)-1)
    op2=data.pop(i2)
    print(f"{op1['name']} is a {op1['description']} from {op1['country']}")
    print(art[1])
    print(f"{op2['name']} is a {op2['description']} from {op2['country']}1"
          f"")
    option=input("Enter your guess 1 or 2\n")
    if  option.isdigit() and (int(option)==2 or int(option)==1):
        option=int(option)
        if option==1:
            if op1['follower_count']>=op2['follower_count']:
                points+=1
                print(f"You are correct \nYou have {points} points")

            else:
                print(f"That is wrong \nYour total points are {points}")
                exit()
        if option==2:
            if op2['follower_count']>=op1['follower_count']:
                points+=1
                print(f"You are correct \nYou have {points} points")
                op1=op2
            else:
                print(f"That is wrong \nYour total points are {points}")
                exit()
    else:
        print("Please enter a number either 1 or 2 ")
        exit()
