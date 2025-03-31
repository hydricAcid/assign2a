import heapq
import math


def parse_input(filename):
    graph = {}
    origin = None
    destinations = []
    node_coords = {}  # for heuristic

    with open(filename, "r") as file:
        lines = file.readlines()
        mode = None

        for line in lines:
            line = line.strip()
            if not line:
                continue

            if line.startswith("Nodes:"):
                mode = "nodes"
            elif line.startswith("Edges:"):
                mode = "edges"
            elif line.startswith("Origin:"):
                mode = "origin"
            elif line.startswith("Destinations:"):
                mode = "destinations"
            else:
                if mode == "nodes":
                    parts = line.split(":")
                    node = int(parts[0].strip())
                    coords = parts[1].strip()[1:-1].split(",")
                    x, y = map(int, coords)
                    node_coords[node] = (x, y)
                    graph[node] = {}  # create graph

                elif mode == "edges":
                    parts = line.split(":")
                    edge = parts[0].strip()[1:-1].split(",")
                    from_node, to_node = map(int, edge)
                    cost = int(parts[1].strip())
                    graph[from_node][to_node] = cost

                elif mode == "origin":
                    origin = int(line)

                elif mode == "destinations":
                    dests = line.split(";")
                    destinations = [int(d.strip()) for d in dests]

    return graph, origin, destinations, node_coords


def heuristic(node, goals, node_coords):
    x1, y1 = node_coords[node]  # current node
    min_distance = float("inf")
    for goal in goals:
        x2, y2 = node_coords[goal]
        distance = abs(x1 - x2) + abs(y1 - y2)  # Manhattan
        if distance < min_distance:
            min_distance = distance
    return min_distance


def a_star(graph, origin, destinations, node_coords):  # find node 4 first //error
    open_set = []
    heapq.heappush(open_set, (0, origin, [origin], 0))  # (f, node, path, g)
    visited = set()
    num_nodes = 0

    while open_set:
        _, current, path, g = heapq.heappop(open_set)
        num_nodes += 1

        if current in destinations:
            return path, num_nodes

        if current in visited:
            continue
        visited.add(current)

        for neighbor, cost in graph[current].items():
            if neighbor not in visited:
                new_g = g + cost
                new_f = new_g + heuristic(neighbor, destinations, node_coords)
                heapq.heappush(open_set, (new_f, neighbor, path + [neighbor], new_g))

    return None, num_nodes


def main():
    import sys

    if len(sys.argv) < 3:
        print("Usage: python main.py <filename> <method> [goal_preference]")
        return

    filename = sys.argv[1]
    method = sys.argv[2]
    goal_preference = (
        int(sys.argv[3]) if len(sys.argv) > 3 else None
    )  # Thêm tham số goal_preference

    graph, origin, destinations, node_coords = parse_input(filename)

    if goal_preference is not None and goal_preference in destinations:
        destinations = [goal_preference]

    if method == "AS":
        path, num_nodes = a_star(graph, origin, destinations, node_coords)
    else:
        print(f"Method {method} not supported yet.")
        return

    print(f"{filename} {method}")
    if path:
        goal = path[-1]
        print(f"{goal} {num_nodes}")
        print(" -> ".join(map(str, path)))
    else:
        print("No path found")


if __name__ == "__main__":
    main()
