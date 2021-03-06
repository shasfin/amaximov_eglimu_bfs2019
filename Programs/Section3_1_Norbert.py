#! /usr/bin/python3
from Section3_1_length_shortest_path import length_shortest_path

# Abschnitt 3.1 -- Abstand zwischen zwei Knoten in Python ausrechnen
# Aufgabe mit Norbert dem Staubsauger-Roboter

# Zimmer von Norbert in der "Liste der Nachbarn"-Darstellung
big_room = {"N" : ["01"],
        "01": ["02"],
        "02": ["12"],
        "03": [],
        "04": [],
        "05": ["06", "15"],
        "06": ["05", "07"],
        "07": ["A"],
        "10": [],
        "11": [],
        "12": ["22"],
        "13": [],
        "14": ["15", "24"],
        "15": ["05", "14"],
        "16": [],
        "A" : ["07"],
        "20": [],
        "21": ["22", "31"],
        "22": ["12", "21", "32"],
        "23": [],
        "24": ["14", "25"],
        "25": ["15", "24", "26"],
        "26": ["25", "36"],
        "27": [],
        "30": [],
        "31": ["21", "32", "41"],
        "32": ["22", "31", "42"],
        "33": [],
        "34": [],
        "35": [],
        "36": ["26", "46"],
        "37": [],
        "40": [],
        "41": ["31", "42", "51"],
        "42": ["32", "41", "43", "52"],
        "43": ["42", "44", "53"],
        "44": ["43", "45", "54"],
        "45": ["44", "46", "55"],
        "46": ["36", "45", "47", "56"],
        "47": ["46"],
        "50": ["51"],
        "51": ["41", "50", "52"],
        "52": ["42", "51", "53"],
        "53": ["43", "52", "54"],
        "54": ["44", "53", "55"],
        "55": ["45", "54", "56"],
        "56": ["46", "55"],
        "57": []}
 
print (length_shortest_path(big_room, "N", "A"))
