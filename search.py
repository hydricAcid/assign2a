import sys
from graph import Graph
from algorithms.a_star import AStar
from algorithms.custom1 import Custom1
from algorithms.custom2 import Custom2
from algorithms.dfs import DepthFirstSearch
from algorithms.GBFS import GreedyBestFirstSearch

def main():
    if len(sys.argv) < 3:
        print("Usage: python search.py <filename> <method> [goal_preference]")
        return

    filename = sys.argv[1]
    method = sys.argv[2].upper()
    goal_preference = int(sys.argv[3]) if len(sys.argv) > 3 else None

    # Parse input and create graph
    graph = Graph()
    graph.parse_input(filename)

    if goal_preference is not None and goal_preference in graph.destinations:
        graph.destinations = [goal_preference]

    # Select algorithm based on method parameter
    if method == "AS":
        algorithm = AStar(graph)
    elif method == "CUS2":
        algorithm = Custom2(graph)
    elif method == "DFS":
        algorithm = DepthFirstSearch(graph)
    elif method == "CUS1":
        algorithm = Custom1(graph)
    elif method == "GBFS":
        algorithm = GreedyBestFirstSearch(graph)
        method = "GreedyBestFirstSearch"
    else:
        print(f"Method {method} not supported yet.")
        return

    # Run algorithm and get results
    path, num_nodes = algorithm.search()

    # Print results
    print(f"{filename} {method}")
    if path:
        goal = path[-1]
        print(f"{goal} {num_nodes}")
        print(" -> ".join(map(str, path)))
    else:
        print("No path found")


if __name__ == "__main__":
    main()
