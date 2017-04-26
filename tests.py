import card_game as cg

new_deck = cg.Deck()
new_deck.shuffle()

john = cg.Hand()
mark = cg.Hand()
zach = cg.Hand()

hands = [john, mark, zach]

print("John: ", john)
print("Mark: ", mark)
print("Zach: ", zach)

new_deck.deal_hands(hands, 5)
print("hands delt")

print("John: ", john)
print("Mark: ", mark)
print("Zach: ", zach)

print("deal and insert card")
card = new_deck.deal_card()
print(card)
print(john)
john.add_card(card)
print(john)

print("remove a card")
print(john)
card = john.hand[3]
print(card)
john.remove_card(card)
print(john)

print("remove a random card")
print(zach)
card = zach.remove_random_card()
print(card)
print(zach)

print("test card equalities")

ace_spades = cg.Card(12, 3)
print(ace_spades)
ace_hearts = cg.Card(12, 2)

print(ace_spades == ace_hearts) # should be false
print(ace_spades.rank_eq(ace_hearts)) # should be true

nine_of_clubs = cg.Card(7,2)

print(nine_of_clubs)
print(nine_of_clubs > ace_spades) # should be false
print(nine_of_clubs < ace_spades) # should be true
