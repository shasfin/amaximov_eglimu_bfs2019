#! /usr/bin/python3

# Abschnitt 3.1 -- Abstand zwischen zwei Knoten in Python ausrechnen

def length_shortest_path(graph, initial, goal):
    queue = [(initial, 0)]
    visited = [initial]
    if initial == goal:
        return 0
    else:
        while queue:
            (node, length) = queue.pop(0)
            newlength = length + 1
            neighbours = graph[node]
            for neighbour in neighbours:
                if neighbour not in visited:
                    queue.append((neighbour, newlength))
                    visited.append(neighbour)
                    if neighbour == goal:
                        return newlength
        return "There is no path between initial and goal in the graph"

