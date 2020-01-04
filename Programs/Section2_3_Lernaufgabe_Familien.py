#! /usr/bin/python3
from Section2_3_Wikipedia import bfs_goal

# Abschitt 2.3 -- Der Algorithmus in Python
# Lernaufgabe
# Alice und Bob untersuchen die Familiendatenbank.
# Teil 4 -- finde heraus, ob sie in derselben Zusammenhangskomponente sind.

def component(graph, initial, goal):
    if goal in bfs_goal(graph, initial, goal):
        print "Der Startknoten und der Zielknoten sind in der gleichen Zusammenhangskomponente"
    else:
        print "Der Startknoten und der Zielknoten sind nicht in der gleichen Zusammenhangskomponente"
