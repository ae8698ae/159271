from building import *


# speed test - use "python optimizer.py" to run
if __name__ == "__main__":
    import timeit
    test_size = 20 # set to 100 to check time for speed race
    t1 = timeit.repeat(stmt="optimizer.max_food(b)", setup="import gc, building, optimizer; "
                                                           "b = building.random_building({0}, True); gc.collect()"
                       .format(test_size), repeat=3, number=1)
    t2 = timeit.repeat(stmt="optimizer.max_supplies(b)", setup="import gc, building, optimizer; "
                                                               "b = building.random_building({0}, False); gc.collect()"
                       .format(test_size), repeat=3, number=1)
    # some calculation that takes ~1 sec on my machine
    tref = timeit.repeat(stmt="for i in range(1000000): a=i^2", setup="import gc; gc.collect()", repeat=3, number=19)
    print("max_food(n={0}) = {1} ({3} normalized), max_supplies(n={0}) = {2} ({4} normalized)"
          .format(test_size, min(t1), min(t2), min(t1) / min(tref), min(t2) / min(tref)))


def max_food(building):
    """returns the maximum number of food that can be collected from given building"""
    solver = []
    for row in range(building.size * 2 + 1):
        solver.append([0 for column in range(building.size * 2 + 1)])

    for column in range(building.size - 1, -1, -1):
        if column == building.size - 1:
            solver[building.size][column] = building.rooms[building.size][column].food
            solver[column][building.size] = building.rooms[column][building.size].food
        else:
            solver[building.size][column] = solver[building.size][column + 1] + building.rooms[building.size][column].food
            solver[column][building.size] = solver[column + 1][building.size] + building.rooms[column][building.size].food

    for column in range(building.size + 1, building.size * 2 + 1):
        if column == building.size + 1:
            solver[building.size][column] = building.rooms[building.size][column].food
            solver[column][building.size] = building.rooms[column][building.size].food
        else:
            solver[building.size][column] = solver[building.size][column - 1] + building.rooms[building.size][column].food
            solver[column][building.size] = solver[column - 1][building.size] + building.rooms[column][building.size].food

    for column in range(building.size - 1, -1, -1):
        for row in range(building.size - 1, -1, -1):
            solver[row][column] = max(solver[row + 1][column], solver[row][column + 1]) + building.rooms[row][column].food
        for row in range(building.size + 1, building.size * 2 + 1):
            solver[row][column] = max(solver[row - 1][column], solver[row][column - 1]) + building.rooms[row][column].food

    for column in range(building.size + 1, building.size * 2 + 1):
        for row in range(building.size - 1, -1, -1):
            solver[row][column] = max(solver[row + 1][column], solver[row][column - 1]) + building.rooms[row][column].food
        for row in range(building.size + 1, building.size * 2 + 1):
            solver[row][column] = max(solver[row - 1][column], solver[row][column - 1]) + building.rooms[row][column].food

    return max(solver[0][0], solver[0][building.size * 2], solver[building.size * 2][0],
               solver[building.size * 2][building.size * 2])




def max_supplies(building):
    """returns the maximum of min(food,water) that can be collected from given building"""

    solver = []
    for row in range(building.size * 2 + 1):
        solver.append([[] for column in range(building.size * 2 + 1)])

    for column in range(building.size - 1, -1, -1):
        if column == building.size - 1:
            solver[building.size][column].append((building.rooms[building.size][column].food, building.rooms[building.size][column].water))
            solver[column][building.size].append((building.rooms[column][building.size].food, building.rooms[column][building.size].water))
        else:
            solver[building.size][column].append((solver[building.size][column + 1][0][0] + building.rooms[building.size][column].food, solver[building.size][column + 1][0][1] + building.rooms[building.size][column].water))
            solver[column][building.size].append((solver[column + 1][building.size][0][0] + building.rooms[column][building.size].food, solver[column + 1][building.size][0][1] + building.rooms[column][building.size].water))

    for column in range(building.size + 1, building.size * 2 + 1):
        if column == building.size + 1:
            solver[building.size][column].append((building.rooms[building.size][column].food, building.rooms[building.size][column].water))
            solver[column][building.size].append((building.rooms[column][building.size].food, building.rooms[column][building.size].water))
        else:
            solver[building.size][column].append((solver[building.size][column - 1][0][0] + building.rooms[building.size][column].food, solver[building.size][column - 1][0][1] + building.rooms[building.size][column].water))
            solver[column][building.size].append((solver[column - 1][building.size][0][0] + building.rooms[column][building.size].food, solver[column - 1][building.size][0][1] + building.rooms[column][building.size].water))

    for column in range(building.size - 1, -1, -1):
        for row in range(building.size - 1, -1, -1):
            to_add = [(supplies[0] + building.rooms[row][column].food, supplies[1] + building.rooms[row][column].water) for supplies in solver[row][column + 1] + solver[row + 1][column]]
            # for supplies in solver[row][column + 1] + solver[row + 1][column]:
            #     to_add.append((supplies[0] + building.rooms[row][column].food, supplies[1] + building.rooms[row][column].water))
            duplicate = set()
            for i in range(len(to_add)):
                if to_add[i] not in duplicate:
                    for j in range(len(to_add)):
                        if j == i:
                            pass
                        elif (to_add[i][0] == to_add[j][0]) and (to_add[i][1] == to_add[j][1]):
                            duplicate.add(to_add[i])
                        elif (to_add[i][0] <= to_add[j][0]) and (to_add[i][1] <= to_add[j][1]):
                            break
                    else:
                        solver[row][column].append(to_add[i])

    for column in range(building.size - 1, -1, -1):
        for row in range(building.size + 1, building.size * 2 + 1):
            to_add = [(supplies[0] + building.rooms[row][column].food, supplies[1] + building.rooms[row][column].water) for supplies in solver[row][column + 1] + solver[row - 1][column]]
            # for supplies in solver[row][column + 1] + solver[row - 1][column]:
            #     to_add.append((supplies[0] + building.rooms[row][column].food, supplies[1] + building.rooms[row][column].water))
            duplicate = set()
            for i in range(len(to_add)):
                if to_add[i] not in duplicate:
                    for j in range(len(to_add)):
                        if j == i:
                            pass
                        elif (to_add[i][0] == to_add[j][0]) and (to_add[i][1] == to_add[j][1]):
                            duplicate.add(to_add[i])
                        elif (to_add[i][0] <= to_add[j][0]) and (to_add[i][1] <= to_add[j][1]):
                            break
                    else:
                        solver[row][column].append(to_add[i])

    for column in range(building.size + 1, building.size * 2 + 1):
        for row in range(building.size - 1, -1, -1):
            to_add = [(supplies[0] + building.rooms[row][column].food, supplies[1] + building.rooms[row][column].water) for supplies in solver[row][column - 1] + solver[row + 1][column]]
            # for supplies in solver[row][column - 1] + solver[row + 1][column]:
            #     to_add.append((supplies[0] + building.rooms[row][column].food, supplies[1] + building.rooms[row][column].water))
            duplicate = set()
            for i in range(len(to_add)):
                if to_add[i] not in duplicate:
                    for j in range(len(to_add)):
                        if j == i:
                            pass
                        elif (to_add[i][0] == to_add[j][0]) and (to_add[i][1] == to_add[j][1]):
                            duplicate.add(to_add[i])
                        elif (to_add[i][0] <= to_add[j][0]) and (to_add[i][1] <= to_add[j][1]):
                            break
                    else:
                        solver[row][column].append(to_add[i])

    for column in range(building.size + 1, building.size * 2 + 1):
        for row in range(building.size + 1, building.size * 2 + 1):
            to_add = [(supplies[0] + building.rooms[row][column].food, supplies[1] + building.rooms[row][column].water) for supplies in solver[row][column - 1] + solver[row - 1][column]]
            # for supplies in solver[row][column - 1] + solver[row - 1][column]:
            #     to_add.append((supplies[0] + building.rooms[row][column].food, supplies[1] + building.rooms[row][column].water))
            duplicate = set()
            for i in range(len(to_add)):
                if to_add[i] not in duplicate:
                    for j in range(len(to_add)):
                        if j == i:
                            pass
                        elif (to_add[i][0] == to_add[j][0]) and (to_add[i][1] == to_add[j][1]):
                            duplicate.add(to_add[i])

                        elif (to_add[i][0] <= to_add[j][0]) and (to_add[i][1] <= to_add[j][1]):
                            break

                    else:
                        solver[row][column].append(to_add[i])

    # for item in solver:
    #     print(item)
    # print()


    return building.size  # dummy implementation - replace
