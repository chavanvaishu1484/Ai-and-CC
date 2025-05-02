import heapq

def dijkstra(graph, start):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    heap = [(0, start)]
    
    while heap:
        current_distance, current_vertex = heapq.heappop(heap)
        
        if current_distance > distances[current_vertex]:
            continue
        
        for neighbor, edge_weight in graph[current_vertex].items():
            distance = current_distance + edge_weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))
    
    return distances

# Example usage
graph = {
    'A': {'B': 2, 'C': 4},
    'B': {'A': 2, 'D': 3},
    'C': {'A': 4, 'D': 1},
    'D': {'B': 3, 'C': 1}
}

start_vertex = 'A'
shortest_distances = dijkstra(graph, start_vertex)
print("Shortest distances from vertex", start_vertex + ":")
for vertex, distance in shortest_distances.items():
    print(f"To vertex {vertex}: {distance}")
