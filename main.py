from keys_and_rooms.solve import canVisitAllRooms
from count_servers_that_communicate.solve import countServers
from network_delay_time.solve import networkDelayTime
from redundant_connection.solve import redundantConnection

if __name__ == "__main__":
    print(f"* Keys and Rooms")
    p1 = [[1],[2],[3],[]]
    s1 = canVisitAllRooms(p1)
    t1 = s1 == True
    print(f"* result={s1}, passing={t1}")

    print("* Servers that can communicate")
    p2 = [[1,0],[1,1]]
    s2 = countServers(p2)
    t2 = s2 == 3
    print(f"* result={s2}, passing={t2}")

    print("* Network Delay Time")
    times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    s4 = networkDelayTime(times,4,2)
    t4 = s4 == 2
    print(f"* result={s4}, passing={t4}")

    print("* Redundant connection")
    p5 = [[1,2], [1,3], [2,3]]
    s5 = redundantConnection(p5)
    t5 = s5 == [2,3]
    print(f"* result={s5}, passing={t5}")