#! /usr/bin/python3

# Abschitt 2.3 -- Der Algorithmus in Python
# Aufgabe 2.5
# Alice und Bob spielen das Wikipedia Spiel

Wikipedia = {
    'B':  ['Z'],
    'BS': ['D', 'G', 'K', 'L'],
    'D':  ['E', 'S'],
    'E':  ['D', 'S', 'U-B'],
    'G':  ['BS', 'K', 'U-B'],
    'K':  ['G'],
    'L':  [],
    'S':  ['D', 'E', 'Z'],
    'SBZ':['B', 'Z'],
    'U-B':['E', 'SBZ'],
    'Z':  ['D', 'S', 'SBZ']
}

def bfs_goal(graph, initial, goal):
    queue = [initial]
    visited = [initial]
    if initial == goal:
        return visited
    else:
        while queue:
            node = queue.pop(0)
            neighbours = graph[node]
            for neighbour in neighbours:
                if neighbour not in visited:
                    queue.append(neighbour)
                    visited.append(neighbour)
                    if neighbour == goal:
                        queue = []
                        break
        return visited

print bfs_goal(Wikipedia, 'BS', 'SBZ')
