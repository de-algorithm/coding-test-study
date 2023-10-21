def survive(info, edges):
    global max_sheep
    node_list = dict()
    for edge in edges:
        node_list[edge[0]] = node_list.get(edge[0], list()) + [edge[1]]
    max_sheep = 0
    
    def travel_tree(node, sheep, wolf, possible):
        global max_sheep
        if info[node] == 1:
            wolf += 1
        else:
            sheep += 1
        if wolf >= sheep:
            return
        max_sheep = max(max_sheep, sheep)
        next_possible = possible+[node]
        neighbors = []
        for x in next_possible:
            neighbors += node_list.get(x, [])
        # print(node, sheep)
        for neighbor in neighbors:
            if neighbor not in next_possible:
                travel_tree(neighbor, sheep, wolf, next_possible)
    travel_tree(0, 0, 0, [])
    return max_sheep