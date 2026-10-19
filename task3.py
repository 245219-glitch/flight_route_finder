flights = {
    "Islamabad": [("Lahore", 40), ("Karachi", 90)],
    "Lahore": [("Karachi", 50), ("Peshawar", 30)],
    "Karachi": [("Quetta", 60)],
    "Peshawar": [("Quetta", 70)],
    "Quetta": [],
}

def path_cost(path):
    return sum(cost for _, cost in path)

def ucs_cheapest_route(graph, start, goal):
    visited = []
    queue = [[(start, 0)]]

    while queue:
        queue.sort(key=path_cost)      
        path = queue.pop(0)
        node = path[-1][0]
        route = [city for city, _ in path]

        print("Exploring:", route, "cost =", path_cost(path))

        if node in visited:
            continue
        visited.append(node)

        if node == goal:
            print("Cheapest route:", route)
            print("Total ticket cost:", path_cost(path))
            return route, path_cost(path)

        for neighbour, cost in graph.get(node, []):
            queue.append(path + [(neighbour, cost)])

    return None, None

ucs_cheapest_route(flights, "Islamabad", "Quetta")