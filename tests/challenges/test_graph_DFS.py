from data_structures_and_algorithms.challenges.depth_first.depth_first import Graph
import pytest
def test_conn():
    pass

def test_new_method_appendded():
    """
    To test if Depth first (dfs) method was appended correctly. I didnt create a new graph to create one new method (waste of time)
    """
    expected = True
    actual = "dfs" in dir(Graph)
    assert expected ==actual


def test_dfs_one_A(pre):
    """
    Test dfs method at start node : 'A'
    """
    expected=['A', 'B', 'C', 'G', 'D', 'E', 'H', 'F']
    actual = pre.dfs(pre,"A")
    assert expected ==actual

def test_dfs_one_F(pre):
    """
    Test dfs method at start node : 'F'
    """
    expected=['F', 'D', 'A', 'B', 'C', 'G', 'E', 'H']
    actual = pre.dfs(pre,"F")
    assert expected ==actual

def test_dfs_one_D(pre):
    """
    Test dfs method at start node : 'D'
    """
    expected=['D', 'A', 'B', 'C', 'G', 'E', 'H', 'F']
    actual = pre.dfs(pre,"D")
    assert expected ==actual



@pytest.fixture
def pre():
    g=Graph()
    g.AddNode("A","B")
    g.AddNode("A","D")
    g.AddNode("B","C")
    g.AddNode("G","C")
    g.AddNode("D","E")
    g.AddNode("D","H")
    g.AddNode("D","F")
    g.AddNode("F","H")

    return g