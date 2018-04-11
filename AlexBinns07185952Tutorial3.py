import random

defensive_cards = []
attack_cards_list = []

card_variable = int(input("How many cards do you want to use? "))

for card in range(card_variable):
    defensive_cards.append((random.randint(1, card_variable), (random.randint(1, card_variable))))
    attack_cards_list.append((random.randint(1, card_variable)))

defensive_cards.sort(key=lambda k: (k[1], -k[0]), reverse=True)

print()
print("List of attack cards")
print(attack_cards_list)
print()
print("List of defensive cards first number is the defense the second number is the card worth")
print(defensive_cards)
print()
print("Its time for the cards to battle")
print()

attack_cards_index = []
match_up = []

for c in range(card_variable + 1):
    attack_cards_index.append(0)

for attack_card in attack_cards_list:
    attack_cards_index[attack_card] += 1

iterator = 0

for card in defensive_cards:
    iterator = card[0]
    while iterator != 0:
        if attack_cards_index[iterator] != 0:
            match_up.append([card, iterator])
            attack_cards_index[iterator] -= 1
            iterator = 0
        elif (attack_cards_index[iterator] == 0) and (sum(attack_cards_index[:(iterator + 1)]) != 0):
            iterator -= 1
        else:
            for max_card in range((len(defensive_cards)), 0, -1):
                if attack_cards_index[max_card] != 0:
                    match_up.append([card, max_card])
                    iterator = 0
                    attack_cards_index[max_card] -= 1
                    break


total = 0
sum_all_cards = sum(x[1] for x in defensive_cards)

for item in match_up:
    if item[0][0] >= item[1]:
        print("Defence Wins with defence of \t{} \tagainst an Attack of \t{}" .format(item[0][0], item[1]))
        total += item[0][1]
    else:
        print("Defence Loses with defence of \t{} \tagainst an Attack of \t{}" .format(item[0][0], item[1]))

print()
print("Defence gets a total of \t{} \tout of a possible \t{}" .format(total, sum_all_cards))
print()
print("List of matched cards")
print(match_up)
