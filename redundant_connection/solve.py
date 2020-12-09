def redundantConnection(edges):
    data = [0]*(len(edges)+1)

    def find_connection(x):
        if data[x] != x:
            data[x] = find_connection(data[x])
        return data[x]

    for edge in edges:
        xEdge, yEdge = map(find_connection, edge)
        if xEdge == yEdge:
            data[min(xEdge, yEdge)] = max(xEdge, yEdge)

    return edge