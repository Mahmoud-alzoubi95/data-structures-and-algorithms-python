from data_structures_and_algorithms.challenges.graph.graph import Graph,Node
import pytest

def test_conn():
    pass

def test_add_1():
    g1=Graph()
    expected = "A node with a and another node with b was added to the graph"
    actual = g1.AddNode("a","b")
    assert expected == actual

def test_add_2():
    g1=Graph()
    expected = "A node with Mohammed and another node with Ghafri was added to the graph"
    actual = g1.AddNode("Mohammed","Ghafri")
    assert expected == actual


def test_addNode():
    g1=Graph()
    expected = "Edg was added successfully between Mohammed and Ghafri with weight = 1"
    actual = g1.AddEdge("Mohammed","Ghafri",1)
    assert expected == actual



def test_getNeighbor():
    g=Graph()
    g.AddNode("a","b")
    g.AddNode("a","c")
    g.AddNode("a","d")  
    g.AddEdge("a","b",800)
    g.AddEdge("a","c",100)
    g.AddEdge("a","d",50)
    actual=g.GetNeighbors("a")
    expected = [('b', 800), ('c', 100), ('d', 50)]
    assert expected ==actual

   

def test_sizer():
    g=Graph()
    g.AddNode("a","b")
    g.AddNode("a","c")
    g.AddNode("a","d")  
    g.AddEdge("a","b",800)
    g.AddEdge("a","c",100)
    g.AddEdge("a","d",50)
    actual=g.Size()
    expected = 6
    assert expected ==actual
