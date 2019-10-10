# for directed graph
from collections import defaultdict


class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, start_node, end_node, distance):
        self.edges[start_node].append(end_node)
        self.distances[(start_node, end_node)] = distance


def create_graph():
    graph_obj = Graph()
    for node in ['A', 'B', 'C', 'D', 'E', 'F']:   # , 'G', 'H', 'I']:
        graph_obj.add_node(node)

    graph_obj.add_edge('A', 'B', 3)
    graph_obj.add_edge('A', 'C', 4)
    graph_obj.add_edge('B', 'C', 6)
    graph_obj.add_edge('B', 'D', 2)
    graph_obj.add_edge('B', 'E', 7)
    graph_obj.add_edge('C', 'E', 5)
    graph_obj.add_edge('D', 'E', 1)
    graph_obj.add_edge('D', 'F', 8)
    graph_obj.add_edge('E', 'F', 4)

    return graph_obj


def dijkstra(graph, first_node):
    visited = {first_node: 0}  # node: distance from first node
    path = {}

    all_nodes = graph.nodes
    all_nodes.remove(first_node)
    current_node = first_node
    current_weight = 0
    while current_node:
        # all the nodes connected from the current node
        next_nodes = graph.edges[current_node]  # a list of nodes
        if next_nodes:
            min_node = None
            for node in next_nodes:
                path[current_node] = next_nodes
                if node not in visited:
                    visited[node] = graph.distances[(current_node, node)] + current_weight
                    if min_node is None:
                        min_node = node
                    elif visited[node] < visited[min_node]:
                        min_node = node

                    all_nodes.remove(node)
                else:
                    temp = graph.distances[(current_node, node)] + current_weight
                    if temp < visited[node]:
                        visited[node] = temp
                        min_node = node

            current_node = min_node
            current_weight = visited[min_node]

        else:  # No more points/ stuck at a point
            break

    return visited, path


if __name__ == "__main__":
    graph_object = create_graph()

    distance_from_first_node, path_from_source_node = dijkstra(graph_object, 'A')
    print('Distance from first node:- ', distance_from_first_node)
    print('Path to all nodes from first node:- ', path_from_source_node)