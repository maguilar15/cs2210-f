# Key and Rooms (Time:  O(n!) Space: O(n))
def canVisitAllRooms(rooms):
    stack = [0]
    mem = set(stack)
    while stack:
        n = stack.pop()
        for e in rooms[n]:
            if e not in mem:
                mem.add(e)
                if len(mem) == len(rooms):
                    return True
                stack.append(e)
    return len(mem) == len(rooms)