import random

"""
    ################
    Classes
    ################
"""

class Card:
    """ A class for a playing card, Card objects created
        during deck class initiation"""

    ranks = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
    suits = ("D", "C", "H", "S")

    def __init__(self, rank, suit):
        self.rank = self.ranks[rank]
        self.suit = self.suits[suit]

    def __str__(self):
        return ("{0}{1}".format(self.rank, self.suit))

    """ eq tests if both rank and suit match
         other equalities only test for ranks
         to test rank equality use self.rank_eq() """
    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

    def rank_eq(self, other):
        return self.rank == other.rank

    def __le__(self, other):
        return self.ranks.index(self.rank) <= self.ranks.index(other.rank)

    def __ge__(self, other):
        return self.ranks.index(self.rank) >= self.ranks.index(other.rank)

    def __gt__(self, other):
        return self.ranks.index(self.rank) > self.ranks.index(other.rank)

    def __lt__(self, other):
        return self.ranks.index(self.rank) < self.ranks.index(other.rank)

    def _ne__(self, other):
        return self.rank != other.rank


class Deck:
    """ A deck of cards, uses Card class for each card object """

    def __init__(self):

        self.rng = random.Random()
        self.deck = []

        for i in range(4):
            for j in range(13):
                self.deck.append(Card(j, i))

    def shuffle(self):
        self.rng.shuffle(self.deck)

    def deal_hands(self, hands, hand_size):
        """ deal out hands for a game
            hands is a list of hand object (player hands)"""
        for i in range(hand_size):
            for j in range(len(hands)):
                card = self.deal_card()
                if str(card) != "None":
                    hands[j].hand.append(card)

    def deal_card(self):
        if self.deck:
            card = self.deck.pop(0)
            return card
        else:
            return None

    def remove_card(self, card):
        if card in self.deck:
            self.deck.remove(card)



class Hand:
    """ class for a hand of cards dealt by Deck and containing Card objects"""

    def __init__(self):
        self.rng = random.Random()
        self.hand = []

    def __str__(self):
        card_list = []
        for card in self.hand:
            card_list.append(str(card))
        return str(card_list)

    def add_card(self, card):
        self.hand.append(card)

    def remove_card(self, card):
        if card in self.hand:
            self.hand.remove(card)

    def remove_random_card(self):
        x = self.rng.randint(0, len(self.hand)-1)
        return self.hand.pop(x)



class Discard(Deck):

    def __init__(self):
        self.rng = random.Random()
        self.discard = []
