

def BellmanFord(nodes, start_node):
    start_node = nodes[start_node]
    print("Starting on node: {}".format(start_node.identifier))
    negative_cycle = False
    path_distances = [[float("inf") for _ in range(len(nodes))] for _ in range(len(nodes))]

    for abc in range(len(nodes)):
        path_distances[abc][start_node.identifier - 1] = 0

    for i in range(len(nodes)):
        for v, n in nodes.items():
            prev_shortest_path = path_distances[i-1][v-1]
            calc_shortest_path = float("inf")
            for e in n.incoming_edges:
                calc_shortest_path = min(calc_shortest_path, path_distances[i-1][e.tail_node.identifier-1]+e.cost)
            path_distances[i][v-1] = min(prev_shortest_path, calc_shortest_path)



    #for k, p in enumerate(path_distances):
    #    print("{}: {}".format(k, p))

    for ff in range(len(nodes)):
        if path_distances[-2][ff] != path_distances[-1][ff]:
            print("Negative Cycle Found: {}".format(ff))
            negative_cycle = True

    if not negative_cycle:
        print("Shortest Shortest Path: {}".format(min(path_distances[-1])))

    return negative_cycle, min(path_distances[-1])

