from collections import deque
from random import randint


def generate_graph(max_siblings, graph_dict):
    if max_siblings is None or graph_dict is None:
        raise ValueError('one of the args is None, max_siblings {} or graph_dict {}'
                         .format(max_siblings, graph_dict))

    if type(graph_dict) != list:
        raise TypeError('passed dictionary is not list type')

    if max_siblings > len(graph_dict) - 2:
        raise ValueError('number of siblings is more than the limit {}'
                         .format(str(len(graph_dict) - 1)))

    graph_map = {}

    # provided connected graph
    for i in range(len(graph_dict)):
        if i + 1 > len(graph_dict) - 1:
            break

        sibling_i = randint(i + 1, len(graph_dict) - 1)

        temp = graph_dict[i + 1]
        graph_dict[i + 1] = graph_dict[sibling_i]
        graph_dict[sibling_i] = temp

        graph_map[graph_dict[i]] = [graph_dict[i + 1]]

    graph_map[graph_dict[i]] = []

    # additional siblings
    for i in range(len(graph_dict)):
        temp = graph_dict[0]
        graph_dict[0] = graph_dict[i]
        graph_dict[i] = temp

        node_values = graph_map[graph_dict[0]]
        esc_v = None
        if len(node_values) > 0:
            esc_v = node_values[0]

        temp_list = [x for x in graph_dict[1:] if not esc_v or x != esc_v]
        n_siblings = randint(0, max_siblings)
        if n_siblings > 0:
            for j in range(n_siblings):

                if len(temp_list) == 1:
                    r_i = 0
                else:
                    r_i = randint(0, len(temp_list) - 1)

                node_values.append(temp_list[r_i])
                temp_list.pop(r_i)

        graph_map[graph_dict[0]] = node_values

        temp = graph_dict[i]
        graph_dict[i] = graph_dict[0]
        graph_dict[0] = temp

    return graph_map


def width_first_search(graph_map, q):
    search_queue = deque()
    checked_nodes_queue = deque()
    long_k = None

    # Primary initialize a query
    for k, v in graph_map.items():
        search_queue.append(k)

    # traverse the graph
    while len(search_queue) > 0 and long_k is None:
        k = search_queue.popleft()
        if len(k) > q:
            long_k = k
        elif k not in checked_nodes_queue:
            checked_nodes_queue.append(k)
            v = graph_map[k]
            if v and len(v) > 0:
                search_queue.append(graph_map[k])

    return long_k
