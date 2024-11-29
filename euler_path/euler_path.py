from collections import defaultdict, deque
from typing import List, Optional


class EulerianPathDirectedEdgesAdjacencyList:
    def __init__(self, graph: List[List[int]]):
        if graph is None:
            raise ValueError("Graph cannot be null")
        self.n = len(graph)
        self.graph = graph
        self.path = deque()
        self.in_degree = [0] * self.n
        self.out_degree = [0] * self.n
        self.edge_count = 0

    def get_eulerian_path(self) -> Optional[List[int]]:
        self._setup()

        if not self._graph_has_eulerian_path():
            return None

        start_node = self._find_start_node()
        self._dfs(start_node)

        # Ensure all edges were traversed; otherwise, the graph is disconnected.
        if len(self.path) != self.edge_count + 1:
            return None

        return list(self.path)

    def _setup(self):
        self.edge_count = 0

        # Compute in-degree and out-degree of each node
        for from_node in range(self.n):
            for to_node in self.graph[from_node]:
                self.out_degree[from_node] += 1
                self.in_degree[to_node] += 1
                self.edge_count += 1

    def _graph_has_eulerian_path(self) -> bool:
        if self.edge_count == 0:
            return False

        start_nodes = end_nodes = 0
        for i in range(self.n):
            if abs(self.out_degree[i] - self.in_degree[i]) > 1:
                return False
            elif self.out_degree[i] - self.in_degree[i] == 1:
                start_nodes += 1
            elif self.in_degree[i] - self.out_degree[i] == 1:
                end_nodes += 1

        return (start_nodes == 0 and end_nodes == 0) or (start_nodes == 1 and end_nodes == 1)

    def _find_start_node(self) -> int:
        start_node = 0
        for i in range(self.n):
            if self.out_degree[i] - self.in_degree[i] == 1:
                return i
            if self.out_degree[i] > 0:
                start_node = i
        return start_node

    def _dfs(self, at: int):
        print(self.out_degree)
        while self.out_degree[at] > 0:
            self.out_degree[at] -= 1
            next_node = self.graph[at][self.out_degree[at]]
            self._dfs(next_node)
        self.path.appendleft(at)

    @staticmethod
    def initialize_empty_graph(n: int) -> List[List[int]]:
        return [[] for _ in range(n)]

    @staticmethod
    def add_directed_edge(graph: List[List[int]], from_node: int, to_node: int):
        graph[from_node].append(to_node)


# Example usage
def example_from_slides():
    n = 7
    graph = EulerianPathDirectedEdgesAdjacencyList.initialize_empty_graph(n)

    edges = [
        (1, 2), (1, 3), (2, 2), (2, 4), (2, 4),
        (3, 1), (3, 2), (3, 5), (4, 3), (4, 6),
        (5, 6), (6, 3)
    ]

    for from_node, to_node in edges:
        EulerianPathDirectedEdgesAdjacencyList.add_directed_edge(graph, from_node, to_node)

    solver = EulerianPathDirectedEdgesAdjacencyList(graph)

    # Outputs path: [1, 3, 5, 6, 3, 2, 4, 3, 1, 2, 2, 4, 6]
    print(solver.get_eulerian_path())


def small_example():
    n = 5
    graph = EulerianPathDirectedEdgesAdjacencyList.initialize_empty_graph(n)

    edges = [
        (0, 1), (1, 2), (2, 3), (3,4), (4,0)
    ]

    for from_node, to_node in edges:
        EulerianPathDirectedEdgesAdjacencyList.add_directed_edge(graph, from_node, to_node)

    solver = EulerianPathDirectedEdgesAdjacencyList(graph)

    # Outputs path: [0, 1, 4, 1, 2, 1, 3]
    print(solver.get_eulerian_path())


if __name__ == "__main__":
    dic1 = {"1": 2, "2": 3}
    dic2 = {"2":3, "1": 2}
    print(dic1 == dic2)
