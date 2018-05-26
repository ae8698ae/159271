import random


def bag_optimizer_single(bag_size, item_weights, values, list_length):
    possibilities = [[0 for x in range(bag_size + 1)] for x in range(list_length + 1)]
    for item_weight_position in range(1, list_length + 1):
        for partial_bag_weight in range(1, bag_size + 1):
            if item_weights[item_weight_position - 1] <= partial_bag_weight:
                possibilities[item_weight_position][partial_bag_weight] = max(
                    values[item_weight_position - 1] + possibilities[item_weight_position - 1][
                        partial_bag_weight - item_weights[item_weight_position - 1]],
                    possibilities[item_weight_position - 1][partial_bag_weight])
            else:
                possibilities[item_weight_position][partial_bag_weight] = \
                    possibilities[item_weight_position - 1][partial_bag_weight]
    return possibilities[list_length][bag_size]


def bag_optimizer_multiple(bag_size, item_weights, values, list_length):
    possibilities = [0 for i in range(bag_size + 1)]
    items = {}
    for i in range(list_length):
        items[item_weights[i]] = values[i]
    for partial_bag_size in range(bag_size + 1):
        bag_value = 0
        for possible in [possible_item for possible_item in item_weights if possible_item <= partial_bag_size]:
            if possible < partial_bag_size:
                remaining_bag = partial_bag_size - possible
                if remaining_bag == possible:
                    possible_bag_value = max(possibilities[partial_bag_size - 1], (items[possible] * 2))
                    if possible_bag_value > bag_value:
                        bag_value = possible_bag_value
                else:
                    possible_bag_value = max(possibilities[partial_bag_size - 1],
                                             (items[possible] + possibilities[remaining_bag]))
                    if possible_bag_value > bag_value:
                        bag_value = possible_bag_value
            elif possible == partial_bag_size:
                if items[possible] > possibilities[partial_bag_size - 1]:
                    if items[possible] > bag_value:
                        bag_value = items[possible]
        possibilities[partial_bag_size] = bag_value
    return possibilities[bag_size]


items_length = random.randint(1, 20)
items_weights = []
item_values = []
for w in range(items_length):
    items_weights.append(random.randint(1, 20))
    item_values.append(random.randint(10, 100))
bag = random.randint(1, 20)

print("For a bag size of", bag)
print("with items and weights of")
print("weight \t value")
for h in range(items_length - 1):
    print(items_weights[h], "\t\t", item_values[h])
print("multiple items in the bag results in a value of",
      bag_optimizer_multiple(bag, items_weights, item_values, items_length))
print("single items in the bag results in a value of",
      bag_optimizer_single(bag, items_weights, item_values, items_length))