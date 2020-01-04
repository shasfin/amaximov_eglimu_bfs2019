#! /usr/bin/python3
# -*- coding: utf-8 -*-

from Section3_2_shortest_path import shortest_path
from Section3_2_shortest_path import backtracking
from more_words import more_words
import string

# Abschnitt 3.2 -- Ein Spaziergang im All

# Aufgabe 3.10

# (a) Die Wörter in der Liste der Nachbarn Darstellung

words = {"ERDE":["EIDE", "ENDE", "ERLE"],
        "EIDE":["EILE", "EINE", "ENDE", "ERDE"],
        "EINE":["EIDE", "EILE", "EINS"],
        "EINS":["EINE", "PINS", "ZINS"],
        "ZINS":["EINS", "PINS", "ZINK", "ZINN"],
        "ZINK":["ZINS", "ZINN", "ZANK", "ZICK"],
        "ZANK":["BANK", "SANK", "ZACK", "ZINK"],
        "ZACK":["ZANK", "PACK", "ZICK", "SACK"],
        "PACK":["ZACK", "SACK", "PARK"],
        "PARK":["PACK", "PARD", "MARK"],
        "MARK":["PARK", "MARS"],
        "MARS":["MARK", "MAUS"],
        "MAUS":["MARS", "HAUS"],
        "HAUS":["MAUS", "HASS"],
        "HASS":["HAUS", "BASS"],
        "BASS":["HASS"],
        "PARD":["PARK"],
        "BAND":["SAND", "BANK"],
        "SAND":["BAND", "SANK"],
        "SACK":["SANK", "ZACK", "PACK"],
        "BANK":["BAND", "SANK", "ZANK"],
        "SANK":["BANK", "ZANK", "SACK", "SAND"],
        "SINN":["ZINN"],
        "ZINN":["SINN", "ZINK", "ZINS"],
        "ZICK":["ZINK", "ZACK"],
        "PINS":["ZINS","EINS"],
        "EILT":["EILE"],
        "EILE":["EINE", "EILT", "EULE"],
        "EULE":["EILE", "ERLE"],
        "ERLE":["EULE", "ERDE"],
        "ENDE":["ERDE", "EIDE", "ENTE"],
        "ENTE":["ENDE"]}
        
# (b) Kürzester Pfad zwischen ERDE und MARS.
print ("Kürzester Pfad zwischen ERDE und MARS:")
print (shortest_path(words, "ERDE", "MARS"))

# (c)* Nachbarn programmatisch berechnen
def compute_neighbours1(nodes, node):
    neighbours = []
    for c1 in string.ascii_uppercase:
        neighbour = c1+node[1:4]
        if neighbour != node:
            if neighbour in nodes:
                neighbours.append(neighbour)
                
    for c2 in string.ascii_uppercase:
        neighbour = node[0]+c2+node[2:4]
        if neighbour != node:
            if neighbour in nodes:
                neighbours.append(neighbour)
    
    for c3 in string.ascii_uppercase:
        neighbour = node[0:2]+c3+node[3:4]
        if neighbour != node:
            if neighbour in nodes:
                neighbours.append(neighbour)
                
    for c4 in string.ascii_uppercase:
        neighbour = node[0:3]+c4
        if neighbour != node:
            if neighbour in nodes:
                neighbours.append(neighbour)
    return neighbours
    
# (Leider haben wir die Wörter im Xxxx Format gesammelt, anstatt vom XXXX Format, der in den Unterlagen eingeführt wird. Deswegen werden wir mit der folgenden Funktion weiterarbeiten).
def compute_neighbours(nodes, node):
    neighbours = []
    for c1 in string.ascii_uppercase:
        neighbour = c1+node[1:4]
        if neighbour != node:
            if neighbour in nodes:
                neighbours.append(neighbour)
                
    for c2 in string.ascii_lowercase:
        neighbour = node[0]+c2+node[2:4]
        if neighbour != node:
            if neighbour in nodes:
                neighbours.append(neighbour)
    
    for c3 in string.ascii_lowercase:
        neighbour = node[0:2]+c3+node[3:4]
        if neighbour != node:
            if neighbour in nodes:
                neighbours.append(neighbour)
                
    for c4 in string.ascii_lowercase:
        neighbour = node[0:3]+c4
        if neighbour != node:
            if neighbour in nodes:
                neighbours.append(neighbour)
    return neighbours
    
print ("Nachbarn von ERDE:")
print (compute_neighbours(more_words, "Erde"))
    
# (d)* Kürzester Pfad zwischen ERDE und MARS, wobei die Nachbarn programmatisch berechnet werden

def bfs_with_parent_neighbours(nodes, initial):
    queue = [initial]
    visited = {initial:None}
    while queue:
        node = queue.pop(0)
        neighbours = compute_neighbours(nodes, node)
        for neighbour in neighbours:
            if neighbour not in visited:
                queue.append(neighbour)
                visited[neighbour] = node
    return visited
    
def shortest_path_neighbours(nodes, initial, goal):
    parents = bfs_with_parent_neighbours(nodes, initial)
    return backtracking(parents, goal)

print ("Kürzester Pfad zwischen Erde und Mond:")
print (shortest_path_neighbours(more_words, "Erde", "Mond"))
