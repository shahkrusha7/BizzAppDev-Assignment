"""
Shortest Path Finder (Dijkstra's Algorithm)

Problem:
Find the shortest path and total distance between two cities in a weighted graph.

Approach:
1. Initialize distances to all cities as infinity, except the start city (0).
2. Visit the closest unvisited city, update distances to its neighbors.
3. Repeat until the destination city is reached.
4. Reconstruct and print the shortest path and its total distance.
"""

def dijkstra(graph, start, destination):
    unvisited = set(graph.keys())
    distance = {city: float('inf') for city in graph}
    previous = {city: None for city in graph}
    distance[start] = 0

    while unvisited:
        current = min((city for city in unvisited), key=lambda city: distance[city])
        unvisited.remove(current)

        if current == destination:
            break

        for neighbor, weight in graph[current].items():
            new_dist = distance[current] + weight
            if new_dist < distance[neighbor]:
                distance[neighbor] = new_dist
                previous[neighbor] = current

    path = []
    city = destination
    while city:
        path.insert(0, city)
        city = previous[city]

    return path, distance[destination]

cities = {
    'A': {'B': 5, 'C': 10},
    'B': {'A': 5, 'C': 3, 'D': 9},
    'C': {'A': 10, 'B': 3, 'D': 1},
    'D': {'B': 9, 'C': 1}
}

start_city = 'A'
destination_city = 'D'

path, dist = dijkstra(cities, start_city, destination_city)
print(f"Shortest path from {start_city} to {destination_city}: {' -> '.join(path)}")
print(f"Total distance: {dist}")
