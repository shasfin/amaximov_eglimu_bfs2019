#! /usr/bin/python3

# Abschnitt 2.3, "Der Algorithmus in Python"

Tramlinien = {
    'B':    ['KH'],
    'C':    ['HE', 'N'],
    'E/U':  ['HE', 'N'],
    'HB':   ['E/U'],
    'HE':   ['C', 'E/U'],
    'HP':   ['KH'],
    'KH':   ['B', 'HP', 'KS', 'N'],
    'KS':   ['E/U', 'KH', 'P'],
    'N':    ['C', 'KH'],
    'P':    ['KS']
}

def bfs(graph, initial):
    queue = [initial]
    visited = [initial]
    while queue:
        node = queue.pop(0)
        neighbours = graph[node]
        for neighbour in neighbours:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.append(neighbour)
    return visited
    
print bfs(Tramlinien, 'KS')
