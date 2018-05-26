from building import *
import building


def max_supplies(building):
    """returns the maximum of min(food,water) that can be collected from given building"""

    def max_finder(quarter, horizontal_cross, vertical_cross):
        previous_column = [[] for i in range(building.size * 2 + 1)]
        current_column = [[] for i in range(building.size * 2 + 1)]
        if quarter == 1:
            for column in range(building.size - 1, -1, -1):
                for row in range(building.size - 1, -1, -1):
                    current_column[0] = [horizontal_cross[column]]
                    if column == building.size - 1:
                        for supplies in [vertical_cross[column]] + current_column[row + 1]:
                            if len(current_column[row]) == 0:
                                current_column[row].append([supplies[0] + building.rooms[row][column].food, supplies[1] + building.rooms[row][column].water])
                            else:
                                to_add = [supplies[0] + building.rooms[row][column].food, supplies[1] + building.rooms[row][column].water]
                                for supply in current_column[row]:
                                    if (supply[0] >= to_add[0]) and (supply[1] >= to_add[1]):
                                        break
                                else:
                                    current_column[row].append(to_add)
                    else:
                        for supplies in previous_column[row] + current_column[row + 1]:
                            if len(current_column[row]) == 0:
                                current_column[row].append([supplies[0] + building.rooms[row][column].food, supplies[1] + building.rooms[row][column].water])
                            else:
                                to_add = [supplies[0] + building.rooms[row][column].food, supplies[1] + building.rooms[row][column].water]
                                for supply in current_column[row]:
                                    if (supply[0] >= to_add[0]) and (supply[1] >= to_add[1]):
                                        break
                                else:
                                    current_column[row].append(to_add)

                previous_column = current_column
                current_column = [[] for i in range(building.size * 2 + 1)]

        elif quarter == 2:
            for column in range(building.size + 1, building.size * 2 + 1):
                for row in range(building.size - 1, -1, -1):
                    current_column[0] = [horizontal_cross[column]]
                    if column == building.size + 1:
                        for supplies in [vertical_cross[column]] + current_column[row + 1]:
                            if len(current_column[row]) == 0:
                                current_column[row].append([supplies[0] + building.rooms[row][column].food, supplies[1] + building.rooms[row][column].water])
                            else:
                                to_add = [supplies[0] + building.rooms[row][column].food, supplies[1] + building.rooms[row][column].water]
                                for supply in current_column[row]:
                                    if (supply[0] >= to_add[0]) and (supply[1] >= to_add[1]):
                                        break
                                else:
                                    current_column[row].append(to_add)
                    else:
                        for supplies in previous_column[row] + current_column[row + 1]:
                            if len(current_column[row]) == 0:
                                current_column[row].append([supplies[0] + building.rooms[row][column].food, supplies[1] + building.rooms[row][column].water])
                            else:
                                to_add = [supplies[0] + building.rooms[row][column].food, supplies[1] + building.rooms[row][column].water]
                                for supply in current_column[row]:
                                    if (supply[0] >= to_add[0]) and (supply[1] >= to_add[1]):
                                        break
                                else:
                                    current_column[row].append(to_add)

                previous_column = current_column
                current_column = [[] for i in range(building.size * 2 + 1)]

        elif quarter == 3:
            for column in range(building.size - 1, -1, -1):
                for row in range(building.size + 1, building.size * 2 + 1):
                    current_column[0] = [horizontal_cross[column]]
                    if column == building.size + 1:
                        for supplies in [vertical_cross[column]] + current_column[row - 1]:
                            if len(current_column[row]) == 0:
                                current_column[row].append([supplies[0] + building.rooms[row][column].food, supplies[1] + building.rooms[row][column].water])
                            else:
                                to_add = [supplies[0] + building.rooms[row][column].food, supplies[1] + building.rooms[row][column].water]
                                for supply in current_column[row]:
                                    if (supply[0] >= to_add[0]) and (supply[1] >= to_add[1]):
                                        break
                                else:
                                    current_column[row].append(to_add)
                    else:
                        for supplies in previous_column[row] + current_column[row - 1]:
                            if len(current_column[row]) == 0:
                                current_column[row].append([supplies[0] + building.rooms[row][column].food, supplies[1] + building.rooms[row][column].water])
                            else:
                                to_add = [supplies[0] + building.rooms[row][column].food, supplies[1] + building.rooms[row][column].water]
                                for supply in current_column[row]:
                                    if (supply[0] >= to_add[0]) and (supply[1] >= to_add[1]):
                                        break
                                else:
                                    current_column[row].append(to_add)

                previous_column = current_column
                current_column = [[] for i in range(building.size * 2 + 1)]

        elif quarter == 4:
            for column in range(building.size + 1, building.size * 2 + 1):
                for row in range(building.size + 1, building.size * 2 + 1):
                    current_column[0] = [horizontal_cross[column]]
                    if column == building.size + 1:
                        for supplies in [vertical_cross[column]] + current_column[row - 1]:
                            if len(current_column[row]) == 0:
                                current_column[row].append([supplies[0] + building.rooms[row][column].food, supplies[1] + building.rooms[row][column].water])
                            else:
                                to_add = [supplies[0] + building.rooms[row][column].food, supplies[1] + building.rooms[row][column].water]
                                for supply in current_column[row]:
                                    if (supply[0] >= to_add[0]) and (supply[1] >= to_add[1]):
                                        break
                                else:
                                    current_column[row].append(to_add)
                    else:
                        for supplies in previous_column[row] + current_column[row - 1]:
                            if len(current_column[row]) == 0:
                                current_column[row].append([supplies[0] + building.rooms[row][column].food, supplies[1] + building.rooms[row][column].water])
                            else:
                                to_add = [supplies[0] + building.rooms[row][column].food, supplies[1] + building.rooms[row][column].water]
                                for supply in current_column[row]:
                                    if (supply[0] >= to_add[0]) and (supply[1] >= to_add[1]):
                                        break
                                else:
                                    current_column[row].append(to_add)

                previous_column = current_column
                current_column = [[] for i in range(building.size * 2 + 1)]


        return previous_column





    horizontal_cross = [[] for i in range(building.size * 2 + 1)]
    vertical_cross = [[] for i in range(building.size * 2 + 1)]


    for negative_iterator in range(building.size - 1, -1, -1):
        print(negative_iterator)
        if negative_iterator == building.size - 1:
            vertical_cross[negative_iterator] = [building.rooms[building.size][negative_iterator].food, building.rooms[building.size][negative_iterator].water]
            horizontal_cross[negative_iterator] = [building.rooms[negative_iterator][building.size].food, building.rooms[negative_iterator][building.size].water]
        else:
            vertical_cross[negative_iterator] = [vertical_cross[negative_iterator + 1][0] + building.rooms[building.size][negative_iterator].food, vertical_cross[negative_iterator + 1][1] + building.rooms[building.size][negative_iterator].water]
            horizontal_cross[negative_iterator] = [horizontal_cross[negative_iterator + 1][0] + building.rooms[negative_iterator][building.size].food, horizontal_cross[negative_iterator + 1][1] + building.rooms[negative_iterator][building.size].water]

    for negative_iterator in range(building.size + 1, building.size * 2 + 1):
        print(negative_iterator)
        if negative_iterator == building.size + 1:
            vertical_cross[negative_iterator] = [building.rooms[building.size][negative_iterator].food, building.rooms[building.size][negative_iterator].water]
            horizontal_cross[negative_iterator] = [building.rooms[negative_iterator][building.size].food, building.rooms[negative_iterator][building.size].water]
        else:
            vertical_cross[negative_iterator] = [vertical_cross[negative_iterator - 1][0] + building.rooms[building.size][negative_iterator].food, vertical_cross[negative_iterator - 1][1] + building.rooms[building.size][negative_iterator].water]
            horizontal_cross[negative_iterator] = [horizontal_cross[negative_iterator - 1][0] + building.rooms[negative_iterator][building.size].food, horizontal_cross[negative_iterator - 1][1] + building.rooms[negative_iterator][building.size].water]

    max_quarter_1 = max_finder(1, horizontal_cross, vertical_cross)
    max_quarter_2 = max_finder(2, horizontal_cross, vertical_cross)
    max_quarter_3 = max_finder(3, horizontal_cross, vertical_cross)
    max_quarter_4 = max_finder(4, horizontal_cross, vertical_cross)
    print(max_quarter_1)

    print(vertical_cross)
    print(horizontal_cross)



if __name__ == "__main__":
    import timeit
    test_size = 20  # set to 100 to check time for speed race
    t2 = timeit.repeat(stmt="optimizer.max_supplies(b)", setup="import gc, building, optimizer; "
                                                               "b = building.random_building({0}, False); gc.collect()".format(test_size), repeat=3, number=1)

    print(t2)