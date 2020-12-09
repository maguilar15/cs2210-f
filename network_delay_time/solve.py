def networkDelayTime(times,N,K):
    computerNetwork = []
    for e in times:                                              # List[List[]]
        fromNode, toNode, timeElapsed = e                        # List[]
        computerNetwork.insert(fromNode,(toNode, timeElapsed))   # insert a TUPLE at position

    arrived = dict()
    resultQueue = set([(0, K)])

    while len(resultQueue) > 0:
        timeElapsed, computerNode = resultQueue.pop()       # (0, K)
        if computerNode not in arrived:
            arrived[computerNode] = timeElapsed
            for nextNode, timeDelay in computerNetwork:
                next_time = timeElapsed + timeDelay
                result = (next_time, nextNode)
                resultQueue.add(result)
    if len(arrived.keys()) == N:
        return max(arrived.values()) - 1
    return 0