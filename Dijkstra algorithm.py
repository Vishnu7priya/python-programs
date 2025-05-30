import heapq
def dijkstra(graph,start):
    queue = [(0,start)]
    dist = { v : float('inf')  for v in graph.keys()}
    dist[start]=0
    v =set()
 
    while queue:
        queue.sort()
        c_w , c_v = heapq.heappop(queue) # 0 , 'A'
        if c_w>dist[c_v]:continue
        for n_v , n_w in graph[c_v]:
            if c_w + n_w < dist[n_v]:
                dist[n_v] = c_w+n_w
                heapq.heappush(queue , ((c_w+n_w , n_v)))
 
    return dist
 
 
graph = {
    'A': [('B', 5), ('C', 1)],
    'B': [('A', 5), ('C', 2), ('D', 1)],
    'C': [('A', 1), ('B', 2), ('D', 4), ('E', 8)],
    'D': [('B', 1), ('C', 4), ('E', 3), ('F', 6)],
    'E': [('C', 8), ('D', 3)],
    'F': [('D', 6)]
}
start = 'A'
res = dijkstra(graph,start)
for i in res.items():
    print(i)
