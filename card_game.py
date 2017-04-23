import random

"""
    ################
    Classes
    ################
"""

class Card:
    """ A class for a playing card, Card objects created by Deck class"""

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return ("{0} of {1}".format(self.rank, self.suit))



class Deck:
    """ A deck of cards, uses Card class for each card object """

    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    suits = ["Hearts", "Clubs", "Diamonds", "Spades"]

    rng = random.Random()

    def __init__(self):

        # deck_location is used to keep track of how many cards
        # have been dealt and is reset after shuffle

        self.deck_location = 0
        self.deck = []
        self.discard = []
        for i in self.suits:
            for j in self.ranks:
                self.deck.append(Card(j, i))

    def shuffle(self):
        self.deck.extend(self.discard)
        self.discard.clear()
        self.rng.shuffle(self.deck)

    def deal_card(self):
        if not self.deck:
            self.rng.shuffle(self.deck)

        if self.deck:
            card = self.deck.pop(0)
        else:
            return "Empty Deck"

        return card

class Hand:
    """ class for a hand of cards dealt by Deck and containing Card objects"""

    def __init__(self, deck, hand_size):
        self.hand = []
        self.deck = deck
        for _ in range(hand_size):
            self.hand.append(self.deck.deal_card())

    def __str__(self):
        card_list = []
        for card in self.hand:
            card_list.append(str(card))
        return str(card_list)

    def remove_card(self, hand_index):
        """ remove a card from hand at given index position """
        # make sure to discard card into deck discard pile
        card = self.hand.pop(hand_index)
        self.deck.discard.append(card)

    def deal_new_card(self):
        """ deal a new card into hand from index position """
        self.hand.append(self.deck.deal_card())

    def add_card(self, card):
        """ add a new card object to hand """
        self.hand.append(card)


"""
    ###############
    Functions
    ###############
"""



""" figure out how to functinize this stuff """

def compare_cards(ranking, p1, p2):
    """ compares the drawn card for each player, if there is a drawn
        "war" will be declared and fuction compare_cards_war() will be called
        --
        the return value is used by logic in the calling function to determine
        who won the comparasin -- if war is declare the return value is used to
        determine why a player one and the number of cards won
    """
    rng = random.Random()
    ranking = ranking
    p1 = p1
    p2 = p2
    p1_card_up = p1.hand.pop(0)
    p2_card_up = p2.hand.pop(0)
    on_the_table = [p1_card_up, p2_card_up]

    p1_ranking = ranking.index(p1_card_up.rank)
    p2_ranking = ranking.index(p2_card_up.rank)

    print("Player one card: {}".format(p1_card_up))
    print("Player two card: {}".format(p2_card_up))

    #rng.shuffle(on_the_table)

    if p1_ranking > p2_ranking:
        p1.hand.extend(on_the_table)
        return("p1")
    elif p2_ranking > p1_ranking:
        p2.hand.extend(on_the_table)
        return("p2")
    else:
        print("\n\n")
        print("War is declared!")
        pauser = input("Press any Key to continue")
        return(compare_cards_war(ranking, p1, p2, on_the_table))


def compare_cards_war(ranking, p1, p2, on_the_table):
    """ compare the drawn cards for each player after "war" is declared
        ranking: a list that contains the ranking order of cards
        p1: player one Hand object
        p2: player two Hand object
        on_the_table: a list of cards on the table to be taken by the winner
        function calls recusively untill either one player runs out of cards
        or a victor of war emerges
        --
        the return value is used by logic in the calling function to determine
        who wan the war, why, and how many cards were won
    """
    rng = random.Random()
    ranking = ranking
    on_the_table = on_the_table
    p1 = p1
    p2 = p2

    if len(p1.hand) < 2:
        return("p2 war p1_empty")
    if len(p2.hand) < 2:
        return("p1 war p2_empty")
    p1_card_up = p1.hand.pop(0)
    p1_card_down = p1.hand.pop(0)
    p2_card_up = p2.hand.pop(0)
    p2_card_down = p2.hand.pop(0)
    on_the_table.extend([p1_card_up, p1_card_down, p2_card_up, p2_card_down])

    p1_ranking = ranking.index(p1_card_up.rank)
    p2_ranking = ranking.index(p2_card_up.rank)

    print("Player one cards: {}, ?????".format(p1_card_up))
    print("Player two cards: {}, ?????".format(p2_card_up))

    #rng.shuffle(on_the_table)

    if p1_ranking > p2_ranking:
        p1.hand.extend(on_the_table)
        return("p1 war {}".format(len(on_the_table)))
    elif p2_ranking > p1_ranking:
        p2.hand.extend(on_the_table)
        return("p2 war {}".format(len(on_the_table)))
    else:
        print("\n\n")
        print("Another war is declared!!")
        pauser = input("Press any key to continue")
        return(compare_cards_war(ranking, p1, p2, on_the_table))



rng = random.Random()
war_ranking = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
new_deck = Deck()
rng.shuffle(new_deck.deck)
player_1 = Hand(new_deck, 26)
player_2 = Hand(new_deck, 26)
game_round = 1

while len(player_1.hand) > 0 and len(player_2.hand) > 0:
    print("\n\n\n\n\n\n\n\n\n\n")
    print("Round {}".format(game_round))
    print("Player One deck size: {0} :: Player Two deck size: {1}".format(len(player_1.hand), len(player_2.hand)))

    print("DUN DUN DUN, Attack!!")
    result = compare_cards(war_ranking, player_1, player_2)
    if len(result) == 2 and result == "p1":
        print("Player One wins cards.")
    elif len(result) == 2 and result == "p2":
        print("Player Two wins cards.")
    elif len(result) > 2 and result[7] == "p":
        if result[:2] == "p1":
            print("Player One wins because Player Two ran out of cards.")
        else:
            print("Player Two wins because Player One ran out of cards.")
        break
    elif len(result) > 2 and result[7] != "p":
        cards_won = result[7:]
        if result[:2] == "p1":
            print("Player One wins {} cards".format(cards_won))
        else:
            print("Player Two wins {} cards".format(cards_won))
    else:
        print("Something went wrong, breaking out of game")
        break

    pauser = input("Press any key for the next round")

    if len(player_1.hand) < 1:
        print("Player Two Has all the cards! Player Two Wins!")
    if len(player_2.hand) < 1:
        print("Player One Has all the cards! Player One Wins!")
    game_round += 1
