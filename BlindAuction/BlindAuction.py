from baart import art
import random
print(art[0])
print("The auction begins for a:")
items =["Catapult","Dragon","Stegosaurus"]
r = random.randint(0,2)
print(f"{items[r]}\n{art[r+1]}")
cont=True
contestants={}
while cont:
    name=input("Enter your name with initial\n")
    bid= int(input("Enter your bid\n"))
    contestants[bid]=name
    x=input("Are there any other bidders: Y,N\n").lower()
    if x=="n":
        cont=False
    print('\n' * 80)# os.system("clear'") doesnt work on pycharm
winner=max(contestants)
print(f"Sold to {contestants[winner]} with a bid of ${winner}\n")
