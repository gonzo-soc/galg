#! /usr/bin/env python3.7

from os import environ
from sys import path

path.append(environ['HOME'] + '/Workspace/Sys/pycharm_projs/galg/')
path.append('.')
path.append('..')

from ds.graph import *

if __name__ == '__main__':

    graph_dict = [
        "Abomination",
        "Apple",
        "Athlete",
        "Angle",
        "Author",
        "Bread",
        "Breath",
        "Board",
        "Bull",
        "Blow",
        "Bit",
        "Bowl",
        "Batery",
        "Corner",
        "Cradle",
        "Camel",
        "Calm",
        "Drive",
        "Disk",
        "Dark",
        "Drill",
        "Dope"
    ]

    share_l = int(3 * len(graph_dict) / 4)

    try:
        graph_map = generate_graph(share_l, graph_dict)
        print("Search a word greater than {}: {}".format(3, width_first_search(graph_map, 3)))
    except TypeError as te_exc:
        print("Error: wrong type passed, wrong type: " + type(graph_dict))
    except ValueError as v_exc:
        print("Error: ValueException exception raised, exception args: " + str(v_exc.args))