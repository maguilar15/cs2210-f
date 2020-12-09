
def countServers(computerGrid):
    rows = [0 for _ in range(len(computerGrid))]
    columns = [0 for _ in range(len(computerGrid[0]))]

    for i in range(len(computerGrid)):
        for j in range(len(computerGrid[0])):
            if computerGrid[i][j]:
                rows[i] += 1
                columns[j] += 1

    predicate = lambda i,j: computerGrid[i][j] and (rows[i] > 1 or columns[j] > 1)

    result = [[i for i in range(len(computerGrid))] for j in range(len(computerGrid[0])) if predicate(i,j)]

    # Plus 1, because we start counting at zero when taking the length of a list.
    return len(result) + 1