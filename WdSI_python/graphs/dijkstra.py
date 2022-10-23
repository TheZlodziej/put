from queue import PriorityQueue
from math import inf

# nodes = {
#     'a': [('g', 5), ('b', 5)],
#     'b': [('a', 5), ('g', 5), ('c', 3), ('d', 3)],
#     'c': [('b', 3), ('d', 1)],
#     'd': [('c', 1), ('b', 3), ('g', 3), ('e', 5), ('f', 4)],
#     'e': [('d', 5), ('f', 2)],
#     'f': [('g', 5), ('d', 4), ('e', 2)],
#     'g': [('a', 5), ('b', 5), ('d', 3), ('f', 5)]
# }

# start_node = 'f'
# end_node = 'c'

nodes = {
    1: [(2, 1), (3, 1)],
    2: [(1, 1), (5, 7)],
    3: [(1, 1), (4, 2)],
    4: [(3, 2), (6, 1)],
    5: [(2, 7), (6, 3), (8, 2)],
    6: [(4, 1), (5, 3), (8, 6), (7, 5)],
    7: [(6, 5)],
    8: [(6, 6), (5, 2)],
}

start_node = 1
end_node = 8
q = PriorityQueue()
q.put((0, start_node))  # wartosc node_id

total_cost = {n: inf for n in nodes}
total_cost[start_node] = 0

parent = {n: None for n in nodes}
visited = set()

while not q.empty():
    _, curr_node = q.get()

    if curr_node in visited:
        continue
    visited.add(curr_node)

    if curr_node == end_node:
        break

    for node, cost in nodes[curr_node]:
        if node in visited:
            continue

        old_cost = total_cost[node]
        new_cost = total_cost[curr_node] + cost
        if new_cost < old_cost:
            total_cost[node] = new_cost
            parent[node] = curr_node
            q.put((new_cost, node))

path = []
curr_node = end_node
while curr_node:
    path.append(curr_node)
    curr_node = parent[curr_node]
path.reverse()

print(path)
