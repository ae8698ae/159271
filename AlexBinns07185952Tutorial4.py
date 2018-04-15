import random


def read_file_traverse_graph(file_name):
    with open(file_name) as f:
        number_of_nodes = int(f.readline().strip())
        start_node = int(f.readline().strip())
        end_node = int(f.readline().strip())
        f.readline()
        graph = [line.strip().split(' ') for line in f if line != '\n']

        for index in range(len(graph)):
            graph[index] = list(map(int, graph[index]))

    count = graph_traversal(start_node, end_node, number_of_nodes, graph)
    return count


def graph_traversal(start_node, end_node, number_of_nodes, graph):
    step_count = 0
    current_index = start_node

    while (current_index != end_node) and (step_count < 2 * number_of_nodes ** 3):
        possible_vertices = []
        for iterator in range(number_of_nodes - 1):
            if graph[current_index][iterator] == 1:
                possible_vertices.append(iterator)

        current_index = random.choice(possible_vertices)
        step_count += 1

    if current_index == end_node:
        return True, step_count
    else:
        return False, step_count


still_more = True

while still_more:
    input_file = input("Please input filename ")
    try:
        result = read_file_traverse_graph(input_file)
        print("For the file {} the traversal returned {} and the number of steps were {}"
              .format(input_file, result[0], result[1]))
    except FileNotFoundError:
        print("That is not a valid filename please try again")
    user_continue = str.lower(input("Do you have another file? (y/n) "))
    if user_continue == 'n':
        still_more = False
