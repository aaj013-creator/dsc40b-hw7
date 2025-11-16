def cluster(graph, weights, level):
    visited = set()
    clusters = []

    for u in graph.nodes:
        if u in visited:
            continue

        stack = [u]
        visited.add(u)
        component = {u}

        while stack:
            x = stack.pop()
            for y in graph.neighbors(x):
                if weights(x, y) >= level and y not in visited:
                    visited.add(y)
                    stack.append(y)
                    component.add(y)

        clusters.append(frozenset(component))

    return frozenset(clusters)
