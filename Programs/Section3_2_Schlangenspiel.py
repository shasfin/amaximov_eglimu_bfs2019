#! /usr/bin/python3
# -*- coding: utf-8 -*-

from Section3_2_shortest_path import shortest_path

# Abschnitt 3.2 -- Kürzester Pfad in Python

# Aufgabe 3.11 -- Bob will das Schlangenspiel gewinnen

# (b) Darstellung als Liste der Nachbarn

snakes_and_ladders = {
        0: [1, 3, 5, 11],
        1: [3, 5, 11],
        2: [3, 5, 6, 11],
        3: [1, 5, 6, 11],
        4: [1, 5, 6, 8],
        5: [1, 6, 8, 9],
        6: [1, 3, 8, 9],
        7: [3, 8, 9, 11],
        8: [3, 9, 11],
        9: [3, 11],
        10: [11],
        11: []
    }
    
# (c) Welche Kästchen wird Bob betreten, wenn er optimal spielt?

print ("shortest_path(snakes_and_ladders, 0, 11):")
print (shortest_path(snakes_and_ladders, 0, 11))

# (e)* Nachbarn programmatisch berechnen

magic_squares = {
        2: 5,
        4: 11,
        7: 1,
        10: 3,
        12: 11,
        13: 11,
        14: 11,
        15: 11
}

def compute_neighbours2(magic_dict, node):
    neighbours = []
    for i in [1, 2, 3, 4]:
        neighbour = node + i
        if neighbour in magic_dict.keys():
            neighbour = magic_dict[neighbour]
        neighbours.append(neighbour)
    return neighbours
    
# (f)* Was muss Bob würfeln?

def compute_neighbours(magic_dict, node):
    neighbours = []
    for i in [1, 2, 3, 4]:
        neighbour = node + i
        if neighbour in magic_dict.keys():
            neighbour = magic_dict[neighbour]
        neighbours.append((neighbour, i))
    return neighbours

def bfs_with_parent_and_dice(magic_dict, initial):
    queue = [initial]
    visited = {initial:(None, None)}
    while queue:
        node = queue.pop(0)
        neighbours_and_die = compute_neighbours(magic_dict, node)
        for (neighbour, dice) in neighbours_and_die:
            if neighbour not in visited:
                queue.append(neighbour)
                visited[neighbour] = (node, dice)
    return visited
    
def backtracking_dice(parents_and_die, goal):
    reversed_path = []
    (node, dice) = parents_and_die[goal]
    while node != None:
        reversed_path.append(dice)
        (node, dice) = parents_and_die[node]
    return list(reversed(reversed_path))
    
def shortest_path_neighbours_and_dice(magic_dict, initial, goal):
    parents = bfs_with_parent_and_dice(magic_dict, initial)
    return backtracking_dice(parents, goal)
    
magic_squares_big = {
    39: 2,
    15: 5,
    17: 22,
    14: 35,
    56: 36,
    42: 55,
    26: 45,
    32: 13,
    9: 11,
    51: 30,
    60: 59,
    61: 59,
    62: 59,
    63: 59,
}

print ("Was muss Bob auf dem grossen Spielfeld würfeln?")
print (shortest_path_neighbours_and_dice(magic_squares_big, 0, 59))

