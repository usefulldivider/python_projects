import random
#nothing is done when a certain card runs out so that will lead to a error
cards = {
    2: 4,
    3: 4,
    4: 4,
    5: 4,
    6: 4,
    7: 4,
    8: 4,
    9: 4,
    10: 16,
    11: 4
}

print("Welcome to ")
print('''
#####    ##         ###     #####   ###  #        ##    ###     #####   ###  #   
##  ##   ##        #####   ###  ##  ### ##        ##   #####   ###  ##  ### ##   
#####    ##        ## ##   ##       #####    ###  ##   ## ##   ##       #####    
##  ##   ##       ##   ##  ##   ##  #####    ###  ##  ##   ##  ##   ##  #####    
##  ###  ##       ##   ##  ###  ##  ######   ###  ##  ##   ##  ###  ##  ######   
#######  #######  ## ####  #######  ### ###  #######  ## ####  #######  ### ###  
######   #######  ## ####  #######  ### ###  #######  ## ####  #######  ### ###  
######   #######  ## ####   #####   ### ###   #####   ## ####   #####   ### ###  
''')
print("DISCLAIMER: THIS PROGRAM IS NOT RULE ACCURATE SOME LIBERTIES HAVE BEEN TAKEN")
def card_reorg(hand, cd):
    for i in cd:
        if i==hand:
            cd[i] -= 1


def total(c):
    total_value = sum(c)
    num_aces = c.count(11)

    while total_value > 21 and num_aces:
        total_value -= 10
        num_aces -= 1

    return total_value


def pprint(c):
    for i in c:
        print(f"{i} ", end=" ")






def blackjack_check(player_total, dealer_total):
    if player_total == 21:
        print("You have a BLACKJACK!\nYou won")
        return True
    elif dealer_total == 21:
        print("The dealer has a BLACKJACK!\nYou lost")
        return True
    elif player_total > 21:
        print(f"You have gone above 21\nTotal:{user_total}\nYou lose")
        return True
    return False


def game_result(player_total, dealer_total):
    if dealer_total > 21:
        print("Dealer lost\nYou win")
    elif dealer_total == 21:
        print("Dealer has 21\nYou lost")
    elif player_total < dealer_total:
        print("You lose")
    elif player_total > dealer_total:
        print("You win")
    else:
        print("It's a draw")


user_cards = random.sample(list(cards), 2)
card_reorg(user_cards[0], cards)
card_reorg(user_cards[1], cards)
# print(cards)
dealer_cards = random.sample(list(cards), 2)
card_reorg(dealer_cards[0], cards)
card_reorg(dealer_cards[1], cards)
# print(cards)

while True:
    print("Your cards:")
    pprint(user_cards)
    print("\nDealer's cards:")
    print(dealer_cards[0])

    user_total = total(user_cards)
    dealer_total = total(dealer_cards)

    if blackjack_check(user_total, dealer_total):
        exit()

    choice = input(f"Do you want to hit? (y/n)\nYour total is {user_total}").lower()
    if choice == "y":
        user_cards.append(random.choice(list(cards)))
        card_reorg(user_cards[len(user_cards)-1], cards)
        # print(cards)

    else:
        break

while dealer_total <= 17:
    dealer_cards.append(random.choice(list(cards)))
    card_reorg(dealer_cards[len(dealer_cards)-1], cards)
    # print(cards)

    # print(dealer_total)
    dealer_total=total(dealer_cards)

print("Dealers cards")
pprint(dealer_cards)
print(f"\ndealers total:{dealer_total}\n")
game_result(user_total, dealer_total)
# print(cards)
