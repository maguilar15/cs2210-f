# Key and Rooms (Time:  O(n!) Space: O(n))
def canVisitAllRooms(rooms):
    stack = [0]
    mem = set(stack)
    while len(stack) > 0:
        node = stack.pop()
        for e in rooms[node]:
            if e not in mem:
                mem.add(e)
                if len(mem) == len(rooms):
                    return True
                stack.append(e)
    return len(mem) == len(rooms)