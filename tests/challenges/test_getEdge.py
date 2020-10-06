# from data_structures_and_algorithms.challenges.graph.graph import Graph
from data_structures_and_algorithms.challenges.get_edge.get_edge import getEdge,Graph
import pytest


def test_conn():
    pass


def test_method_appending():
    """
    To test if getEdge method was appended correctly. I didnt create a new graph to create one new method (waste of time)
    """
    expected = True
    actual = "getEdge" in dir(Graph)
    assert expected ==actual


def test_trip_one(pre):
    actual=pre.getEdge(pre,['Arendelle', 'New Monstropolis', 'Naboo'])
    expected = 'True, $115'
    assert actual ==expected

def test_trip_two(pre):
    actual=pre.getEdge(pre,['Metroville', 'Pandora'])
    expected = 'True, $82'
    assert actual ==expected

def test_trip_3(pre):
    actual=pre.getEdge(pre,['Naboo', 'Pandora'])
    expected = 'False, $0'
    assert actual ==expected


def test_trip_4(pre):
    actual=pre.getEdge(pre,['Narnia', 'Arendelle', 'Naboo'])
    expected = 'False, $0'
    assert actual ==expected



@pytest.fixture
def pre():

    g=Graph()
    # g1=Graph()
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
    return g

