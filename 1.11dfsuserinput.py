def depthFirstSearch(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            depthFirstSearch(visited, graph, neighbour)

def create_graph():
    graph = {}
    edges = int(input("Enter the number of edges: "))
    print("Enter the edges in the format 'source destination', separated by space:")
    for _ in range(edges):
        source, destination = input().split()
        if source not in graph:
            graph[source] = []
        if destination not in graph:
            graph[destination] = []
        graph[source].append(destination)
        graph[destination].append(source)  # For undirected graph
    return graph

print("Create your tree:")
graph = create_graph()
visited = set()
print("\nDepth-First Search:")
depthFirstSearch(visited, graph, '1')
