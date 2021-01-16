import random
import art
import replit

############### Blackjack Project #####################
############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

def dealCard():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculateScore(cardList):
    """Returns the total of elements in the card-list"""
    if sum(cardList) == 21 and len(cardList) == 2:
        return 1
    if 11 in cardList and sum(cardList) > 21:
        cardList[cardList.index(11)]=1
    return sum(cardList)

def compare(userScore, compScore):
    """Compares the scores of the two inputs"""
    if userScore == compScore:
        return "\nGame Draw\n"
    elif compScore == 0:
        return "\nOpponent has a BlackJack. You Lose\n"
    elif userScore ==0:
        return "\nYou Win with a BlackJack\n"
    elif userScore > 21:
        return "\nYou went over. You Lose\n"
    elif compScore > 21:
        return "\nOpponent went over. You Win\n"
    elif userScore > compScore:
        return "\nYou Win\n"
    else:
        return "\nYou Lose\n"

def blackJack():
    """Driver Code"""
    replit.clear()
    print(art.logo)

    userCards.clear()
    compCards.clear()

    for i in range(2):
        userCards.append(dealCard())
        compCards.append(dealCard())

    while True:
        userScore = calculateScore(userCards)
        compScore = calculateScore(compCards)
        print(f"\nYour cards : {userCards}, your current score = {userScore}")
        print(f"Computer's first card : {compCards[0]}")

        if userScore > 21 or userScore == 0 or compScore == 0:
            break
        else:
            drawAnotherCard = input("\nDo you want to draw another card? Type 'y' or 'n': ").lower()
            if drawAnotherCard == 'y':
                userCards.append(dealCard())
                userScore = calculateScore(userCards)
                compScore = calculateScore(compCards)
            else:
                break

    while compScore < 17 and compScore != 0:
        compCards.append(dealCard())
        compScore = calculateScore(compCards)

    print(f"\nYour final hand : {userCards}, your final score = {userScore}")
    print(f"Computer's final hand : {compCards}, computer's final score = {compScore}")
    print(compare(userScore, compScore))

    yesOrNo = input("Do you wanna play a game of BlackJack? Type 'y' or 'n': ").lower()
    if yesOrNo != 'y':
        print("\nGoodbye")
        return 
    blackJack()


userCards = []
compCards = []

blackJack()
