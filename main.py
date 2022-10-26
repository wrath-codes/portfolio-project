import requests
import random
import time
# New Project to Read Tarot Cards and give a reading
# Card function


class Card:
    def __init__(self, value, name, meaning_up, meaning_rev):
        self.value = value
        self.name = name
        self.meaning_up = meaning_up
        self.meaning_rev = meaning_rev

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


# Deck function
url = "https://rws-cards-api.herokuapp.com/api/v1/cards"
response = requests.get(url)
response_json = response.json()
cards_to_iterate = response_json['cards']

cards = []
for card in cards_to_iterate:
    cards.append(Card(card['value'], card['name'],
                 card['meaning_up'], card['meaning_rev']))

picked_cards = []


def pick_card():
    card = random.choice(cards)
    if card in picked_cards:
        pick_card()
    else:
        picked_cards.append(card)
        return card


def pick_side():
    return random.choice(['up', 'rev'])


def main():
    # Program must interact with user
    # Program will greet the user
    print("Hello, I am the Tarot Card Reader. I will read your cards for you.")

    # Program will start with the user's name
    name = input("What is your name? ")

    # Program will ask the user if they want a reading
    time.sleep(1)
    reading = input("Would you like a reading? yes or no? ")
    if reading == "yes":
        print("Ok, I will read your cards.")
    else:
        print("Ok, maybe next time.")
        exit()

    # Program will shuffle the deck
    print("Shuffling the deck...")
    time.sleep(1)

    # Program will pick 3 cards
    print("Picking 3 cards...")
    time.sleep(1)

    # Program will pick the first card
    card1 = pick_card()
    side1 = pick_side()

    # Program will pick the second card
    card2 = pick_card()
    side2 = pick_side()

    # Program will pick the third card
    card3 = pick_card()
    side3 = pick_side()

    # Program will start the reading
    print("Ok, here is your reading.")
    time.sleep(1)

    # Program will print the first card
    print("Let's start with your past.")
    time.sleep(1)
    meaning_1 = card1.meaning_up if side1 == 'up' else card1.meaning_rev
    side_option_1 = "up" if side1 == 'up' else "reversed"
    print("The first card is the {card1.name} card. It is {side_option_1}.".format(
        card1=card1, side_option_1=side_option_1))
    # The meaning of the card
    time.sleep(1)
    print("The meaning of the card is {meaning_1}.".format(
        meaning_1=meaning_1))

    # Program will print the second card
    print("Let's move on to your present.")
    time.sleep(1)
    meaning_2 = card2.meaning_up if side2 == 'up' else card2.meaning_rev
    side_option_2 = "up" if side2 == 'up' else "reversed"
    print("The second card is the {card2.name} card. It is {side_option_2}.".format(
        card2=card2, side_option_2=side_option_2))
    # The meaning of the card
    time.sleep(1)
    print("The meaning of the card is {meaning_2}.".format(
        meaning_2=meaning_2))

    time.sleep(2)

    # Program will print the third card
    print("Let's finish with your future.")
    time.sleep(1)
    meaning_3 = card3.meaning_up if side3 == 'up' else card3.meaning_rev
    side_option_3 = "up" if side3 == 'up' else "reversed"
    print("The third card is the {card3.name} card. It is {side_option_3}.".format(
        card3=card3, side_option_3=side_option_3))
    # The meaning of the card
    time.sleep(1)
    print("The meaning of the card is {meaning_3}.".format(
        meaning_3=meaning_3))
    time.sleep(1)

    # Program will thank the user
    print("Thank you for your time. I hope you enjoyed your reading.")


if __name__ == "__main__":
    main()
