import queue

edges = {
    1: [2, 3],
    2: [1, 3, 4],
    3: [1, 2, 4, 6, 8],
    4: [2, 3, 5],
    5: [4, 7],
    6: [3, 8],
    7: [5, 8, 9],
    8: [6, 3, 7, 9],
    9: [7, 8],
}

start_edge = 1
end_edge = 8

current_edge = start_edge
edges_queue = queue.Queue()
edges_queue.put(start_edge)
visited = [False for _ in enumerate(edges)]
visited[start_edge - 1] = True
previous_edge = [-1 for _ in enumerate(edges)]

while current_edge != end_edge:
    current_edge = edges_queue.get()

    for edge in edges.get(current_edge):
        if not visited[edge - 1]:
            edges_queue.put(edge)
            visited[edge - 1] = True
            previous_edge[edge - 1] = current_edge

path = []
while current_edge != -1:
    path.append(current_edge)
    current_edge = previous_edge[current_edge - 1]
path.reverse()

print(path)
