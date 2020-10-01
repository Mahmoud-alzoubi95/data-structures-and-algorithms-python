from queue import Queue

class Node:
    def __init__(self, value):
        self.value = value
        # self.neighbors = []


# [
#     node(val, []),
#     node(val, []),
#     node(val, [])
# ]

# {
#     node1: [],
#     node2: [],
#     ....
# }

class Graph:
    def __init__(self):
        self._adjacency_list = {}

    def add_node(self, value):
        node = Node(value)
        # self._adjacency_list.push(node)
        self._adjacency_list[node] = []

    def add_edge(self, start_node, end_node, weight=1):
        pass

    def get_nodes(self):
        return self._adjacency_list.keys()

    def get_neighbors(self, node):
        pass

    def size(self):
        pass

    def bfs(self, start_node):
        q = Queue()
        q.enqueue(start_node)
        while len(q):
            cur = q.dequeue()
            # mark the node as visited so you don't enqueue(visit) it again
            print(cur.value)
            neighbors = self._adjacency_list[cur]
            for n in neighbors:
                q.enqueue(n)

    def dfs(self, start_node):
        pass

if __name__ == "__main__":
    g = Graph()