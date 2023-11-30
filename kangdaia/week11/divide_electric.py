from collections import defaultdict


def electric_network(n: int, wires: list[list[int]]) -> int:
    nodes = defaultdict(list)
    res = float('inf')
    for s, e in wires:
        nodes[s].append(e)
        nodes[e].append(s)

    def dfs(node: int, visited: set()):
        visited.add(node)
        for child in nodes[node]:
            if child not in visited:
                visited = dfs(child, visited)
        return visited

    for i in nodes:
        for j in nodes[i]:
            temp = set()
            temp.add(i)
            record = dfs(j, temp)
            diff = abs((n - (len(record) - 1)) - (len(record) - 1))
            res = min(res, diff)

    return res
