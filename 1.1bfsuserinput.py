def breadthFirstSearch(graph, start):
    visited = []
    queue = []
    visited.append(start)
    queue.append(start)

    while queue:
        m = queue.pop(0)
        print(m, end=" ")

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

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
start_node = input("Enter the starting node for BFS traversal: ")
print("\nBreadth-First Search:")
breadthFirstSearch(graph, start_node)
