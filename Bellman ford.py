edges=[
    (0,1,6),
    (0,2,7),
    (1,2,8),
    (1,3,5),
    (1,4,-4),
    (2,3,-3),
    (2,4,9),
    (3,1,-2),
    (4,0,2),
    (4,3,7)]

def bellmen_ford(edges,v,source):
    distances = [float("inf")]*v
    distances[source] = 0

    for i in range(v-1):
        for u,v,c in edges:
            if distances[u] + c < distances[v]:
                distances[v] = distances[u]+c

    return distances

print(bellmen_ford(edges,5,0))
