#! /usr/bin/python3
from Section3_1_length_shortest_path import length_shortest_path

# Abschnitt 3.1 -- Abstand zwischen zwei Knoten in Python ausrechnen

# Aufgabe 3.5
# Ueber wie vielen Ecken kennt jeder jeden?

friends = {"A":["B", "G"],
        "B":["A", "C", "D"],
        "C":["B", "E", "F"],
        "D":["B"],
        "E":["C", "F"],
        "F":["C", "E", "G", "J"],
        "G":["A", "F", "H", "J"],
        "H":["G", "J"],
        "J":["F", "G", "H", "L"],
        "L":["J"]}
        
print (length_shortest_path(friends, "D", "L"))

def length_all_shortest_paths_from(graph, initial):
    queue = [(initial, 0)]
    visited = {initial: 0}
    while queue:
        (node, length) = queue.pop(0)
        newlength = length + 1
        neighbours = graph[node]
        for neighbour in neighbours:
            if neighbour not in visited.keys():
                queue.append((neighbour, newlength))
                visited[neighbour] = newlength
    return visited
    
def diameter(graph):
    maximum = (0, "from", "to")
    for node in graph.keys():
        all_shortest_from = length_all_shortest_paths_from(graph, node)
        maximum_from = max(all_shortest_from, key=all_shortest_from.get)
        if (all_shortest_from[maximum_from] > maximum[0]):
            maximum = (all_shortest_from[maximum_from], node, maximum_from)
    return maximum
    
print (diameter(friends))
