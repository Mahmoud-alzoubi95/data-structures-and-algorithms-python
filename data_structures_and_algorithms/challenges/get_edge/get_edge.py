# from data_structures_and_algorithms.challenges.graph.graph import Graph
# from data_structures_and_algorithms.challenges.graph.queue import Queue
from data_structures_and_algorithms.challenges.breadth_first.breadth_first import Graph


def getEdge(self,graph,arr):
    keys=list(graph.adjacency_list.keys())

    cost=0
    for x,i in enumerate(arr):
        if x+1 == len(arr):
            break
        if arr[x+1] in graph.adjacency_list[i] :
            # print("YEs")
            cost +=graph.getweight(i,arr[x+1])

        else:
            return 'False, $0'
    cost = '$'+ str(cost)
    print(cost)
    return f'True, {cost}'


# Assign getEdge function to be a class method for Graph
Graph.getEdge=getEdge




if __name__ == "__main__":

    g=Graph()
    g1=Graph()
    g.AddNode("Pandora","Metroville")
    g.AddNode("Pandora","Arendelle")
    g.AddNode("Arendelle","Metroville")    
    g.AddNode("Arendelle","New Monstropolis")
    g.AddNode("Metroville","New Monstropolis")  
    g.AddNode("Metroville","Narnia") 
    g.AddNode("Metroville","Naboo")
    g.AddNode("New Monstropolis","Naboo")
    g.AddNode("Narnia","Naboo")

    g.AddEdge("Pandora","Metroville",82)
    g.AddEdge("Pandora","Arendelle",150)
    g.AddEdge("Arendelle","Metroville",99)    
    g.AddEdge("Arendelle","New Monstropolis",42)
    g.AddEdge("Metroville","New Monstropolis",105)  
    g.AddEdge("Metroville","Narnia",37) 
    g.AddEdge("Metroville","Naboo",26)
    g.AddEdge("New Monstropolis","Naboo",73)
    g.AddEdge("Narnia","Naboo",250)
    print(g.edgs)
    print(g.getEdge(g,['Arendelle', 'New Monstropolis', 'Naboo']))

    # print(list(g.adjacency_list.keys()))
    # print(g.adjacency_list)