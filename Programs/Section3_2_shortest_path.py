#! /usr/bin/python3
# -*- coding: utf-8 -*-

# Abschnitt 3.2 -- Der kürzeste Pfad in Python

def bfs_with_parent(graph, initial):
    queue = [initial]
    visited = {initial:None}
    while queue:
        node = queue.pop(0)
        neighbours = graph[node]
        for neighbour in neighbours:
            if neighbour not in visited:
                queue.append(neighbour)
                visited[neighbour] = node
    return visited

numbers = {0: [1, 2],
        1: [0, 3, 4],
        2: [0, 3],
        3: [1, 2, 4],
        4: [1, 3, 5, 6, 7],
        5: [4, 9],
        6: [4, 7, 8, 10],
        7: [4, 6, 10],
        8: [6, 9],
        9: [5, 8],
        10:[6, 7]}
        
print ("bfs_with_parent(numbers, 0):")
print (bfs_with_parent(numbers, 0))
    
def backtracking(parents, goal):
    reversed_path = []
    node = goal
    while node != None:
        reversed_path.append(node)
        node = parents[node]
    return list(reversed(reversed_path))

# Aufgabe 3.8 -- Kombiniere bfs_with_parent und backtracking um den kürzesten Pfad auszurechnen.
    
def shortest_path(graph, initial, goal):
    parents = bfs_with_parent(graph, initial)
    return backtracking(parents, goal)
