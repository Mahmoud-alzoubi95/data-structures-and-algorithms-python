from data_structures_and_algorithms.challenges.get_edge.get_edge import Graph

# print(dir(Graph))

def depthFirstSearch(self,graph,node):

    visited=[]
    def _walk(graph,node):
        visited.append(node)
        for node in graph.adjacency_list[node]:
            if node not in visited:
                _walk(graph,node)
    
    _walk(graph,node)
    return visited


Graph.dfs=depthFirstSearch




if __name__ == "__main__":
    g=Graph()
    g.AddNode("A","B")
    g.AddNode("A","D")
    g.AddNode("B","C")
    g.AddNode("G","C")
    g.AddNode("D","E")
    g.AddNode("D","H")
    g.AddNode("D","F")
    g.AddNode("F","H")
    print(g.adjacency_list)
    print(g.dfs(g,"D"))


