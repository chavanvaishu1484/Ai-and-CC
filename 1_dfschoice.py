def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    print(start, end=" ")

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

def bfs(graph, start):
    visited = set()
    queue = [start]
    visited.add(start)

    while queue:
        node = queue.pop(0)
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

graph = {
    0: [1, 2],
    1: [3, 4],
    2: [],
    3: [],
    4: []
}

while True:
    print("\nMenu:")
    print("1: BFS")
    print("2: DFS")
    print("3: Exit")
    
    choice = int(input("Enter your choice (1/2/3): "))
    
    if choice == 1:
        print("BFS executed:")
        bfs(graph, 0)
    elif choice == 2:
        print("DFS executed:")
        dfs(graph, 0)
    elif choice == 3:
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
