import random

def randomised_st_connectivity(file_name):
    with open(file_name) as f:
        number_of_nodes = int(f.readline().strip())
        start_node = int(f.readline().strip())
        end_node = int(f.readline().strip())
        f.readline()
        graph = [line.strip().split(' ') for line in f if line != '\n']

        for i in range(len(graph)):
            graph[i] = list(map(int, graph[i]))

    count = graph_traversal(start_node, end_node, number_of_nodes, graph)

    return count


def graph_traversal(start_vertice, end_vertice, number_of_nodes, graph):

    step_count = 0
    current_index = start_vertice

    while (current_index != end_vertice) and (step_count < 2 * number_of_nodes ** 3):
        possible_vertices = []
        for iterator in range(number_of_nodes - 1):
            if graph[current_index][iterator] == 1:
                possible_vertices.append(iterator)

        current_index = random.choice(possible_vertices)
        print(current_index)
        step_count += 1
    if current_index == end_vertice:
        return(True, step_count)
    else:
        return (False, step_count)


print(randomised_st_connectivity("testgraph7.txt"))
