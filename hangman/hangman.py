import random
from hangmannecessities import stages,wordlist
print(stages[7])
word=random.choice(wordlist)

gword=[]
for i in word:
    gword.append("_")

life=7
c=6

def gwordp():
    for i in gword:
        print(i,end=" ")
gwordp()
guessed=""
while "_" in gword:
    print(f"\nthe guesses letters are{guessed}")
    a=input("\nEnter the letter").lower()
    guessed+=(" "+a)
    if a not in word:

        print(stages[c])
        life -= 1
        c-=1
        if life==0:
            print(f"The word was {word}")
            print(stages[8])

            exit()

    else:
        if a in gword :
            print(f"you have guessed {a} already")
        else:
            for i in range(len(word)):
                if a==word[i]:
                    gword[i]=a
    gwordp()


if "_" not in gword:
    print(stages[9])

