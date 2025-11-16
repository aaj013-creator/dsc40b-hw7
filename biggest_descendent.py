def biggest_descendent(graph, root, value):
    biggest = {}

    def dfs(u):
        best = value[u]
        for v in graph.out_neighbors(u):
            child_best = dfs(v)
            if child_best > best:
                best = child_best
        biggest[u] = best
        return best

    dfs(root)
    return biggest
