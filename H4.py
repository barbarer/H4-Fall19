import random
import unittest

## Name :
## People you worked with :
## Github URL :

class Card:
    ''' Represents a standard playing card '''

    suit_names = ["Clubs", "Diamonds", "Hearts", "Spades"]
    rank_names = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

    def __init__(self, rank=0, suit=0):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return Card.rank_names[self.rank] + " of " + Card.suit_names[self.suit]

    def compare_card(self, card):
        if self.rank < card.rank:
            return -1
        elif self.rank > card.rank:
            return 1
        else:
            return 0
    # EXTRA CREDIT
    ## Update the compare_card method to consider the suits of cards when two cards have same ranks:
    ## Suits are in this order : Clubs < Spades < Hearts < Diamonds
    ## Therefore, a ''2 of Clubs'' is lower than a ''2 of Spades'' but a ''9 of Hearts'' is higher than a ''8 of Diamonds''


class Deck:
    ''' Represents a deck of cards '''

    def __init__(self):
        self.card_list = []
        for i in range(len(Card.suit_names)):
            for j in range(len(Card.rank_names)):
                self.card_list.append(Card(suit=i,rank=j))

    def __str__(self):
        output = ""
        for card in self.card_list:
            output += card.__str__() + ", "
        return output

    def shuffle(self):
        return random.shuffle(self.card_list)

    def draw_card(self):
        return self.card_list.pop()

    def add_card(self, card_instance):
        randix = random.randrange(len(self.card_list))
        self.card_list.insert(randix, card_instance)



class Player:
    ''' Represents a player who is dealt a hand of cards '''
    pass
    # 1. Create the constructor
    ### A player object should have 3 instance variables : name (str); hand (list); score (int)
    ### It takes 3 inputs - card deck, the name of the player, and the number of cards to be dealt.
    ### By default, a player should be given 5 cards.
    ### It also sets the player's score to zero
    ### It should randomly draw the number of cards specified in input from a shuffled deck
    ### and append the cards to a list called hand

    # 2. Create the __str__ method
    ### It returns the player's name, number of cards remaining in the hand and the current score
    ### For example, "Leo : 3 cards in hand. 0 points"

    # 3. Create the play_card method
    ### It should remove the last card from the player's hand and return it

    # 4. Create the update_score method
    ### It should take an integer as the input (-1, 0, +1) and then add it to the
    ### player's score to update their score

    # 5. Create final_score method
    ### Takes another Player object as the input
    ### It compares the scores of both players
    ### Returns the name of the player who won. For example, ''Leo won by 2 points''
    ### If the players scores are equal, returns ''No winners!''

    # 6. Create the exchange_card method
    ### It takes as input a card deck from which cards were dealt to players
    ### The player can can exchange the last card in their hand (the card at the
    ### last index in their hand) with a card drawn from the deck.



class TestAllMethods(unittest.TestCase):
    ## Check if the last card of the deck is 'King of Spades'
    def test_deck_last_card(self):
        d = Deck()
        self.assertEqual(str(d.card_list[-1]),'King of Spades')

    ## Check if the new deck has 52 cards
    def test_deck_length(self):
        self.assertEqual(len(Deck().card_list), 52)

    ## Check that a deck is left with 47 cards, after 5 cards are dealt to a player
    def test_length_after_deal(self):
        d = Deck()
        p = Player(d, 'Jim')
        self.assertEqual(len(d.card_list),47)

    # Check that the deck has same number of cards after a card is exchanged
    def test_length_exchange_card(self):
        d = Deck()
        p = Player(d, 'Jim')
        p.exchange_card(d)
        self.assertEqual(len(d.card_list),47)

    # Check that suits are used as a tie breaker
    # It is ok for this test case to fail if you did not attempt the extra credit
    def test_extra_credit(self):
        card1 = Card(rank=0, suit=0)
        card2 = Card(rank=0, suit=1)
        card3 = Card(rank=7, suit=3)
        card4 = Card(rank=10, suit=0)
        self.assertEqual(card1.compare_card(card2), -1)
        self.assertEqual(card2.compare_card(card1), 1)
        self.assertEqual(card3.compare_card(card4), -1)
        self.assertEqual(card4.compare_card(card3), 1)


def main():
    ### Creates a deck object and shuffles it
    card_deck = Deck()
    card_deck.shuffle()

    # Complete this...
    ### Create two player objects with the right inputs : They should both be dealt 7 cards each.
    hand_length = 7
    player1 =
    player2 =

    # Complete this...
    ### Both players should play their cards in alternation (one after the other)
        ### print the card that was played
        ### Compare their cards and update their scores
        ### Print the player information (call __str__)
        ### Before playing the final cards both players should exchange their final cards 
    for c in range(0,hand_length):
        pass
    print("\n")

    ### Print which player won using the final_score method


if __name__ == "__main__":
    main()
    print("\n")
    unittest.main(verbosity = 2)
