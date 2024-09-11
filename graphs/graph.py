class Graph:
    def __init__(self, num_of_nodes, directed=False):
        self.m_num_of_nodes = num_of_nodes
        self.m_nodes = range(self.m_num_of_nodes)
        self.m_directed = directed
        self.m_adj_list = {node: set() for node in self.m_nodes}
        self.m_adj_matrix = [[0 for _ in self.m_nodes] for _ in self.m_nodes]

    def add_edge(self, node1, node2):
        self.m_adj_list[node1].add(node2)
        self.m_adj_matrix[node1][node2] = 1
        if not self.m_directed:
            self.m_adj_list[node2].add(node1)
            self.m_adj_matrix[node2][node1] = 1

    def print_adj_list(self):
        print(self.m_adj_list)

    def print_adj_matrix(self):
        print(self.m_adj_matrix)


# test code
# graph = Graph(5)
# graph.add_edge(0, 1)
# graph.add_edge(1, 2)
# graph.add_edge(2, 3)
# graph.add_edge(2, 4)
# graph.add_edge(3, 4)
# graph.print_adj_list()
# graph.print_adj_matrix()
