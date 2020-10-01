def tree_intersection(bt1, bt2):
  common_values = []

  def _traverse(node1, node2):
    if node1 is None or node2 is None:
      return

    if node1.value == node2.value:
      common_values.append(node1.value)

    _traverse(node1.left, node2.left)
    _traverse(node1.right, node2.right)
  
  _traverse(bt1.root, bt2.root)
  return common_values

"""
ref (https://repl.it/@MohammedGhafri/tree-intersection)

            2                     4
        6      -1             6       9
                  8         5   1   5   8
  
[6, 8]

Recursion Visualization:
[]
1. _travese(node(2), node(4))

      2. _travese(node(6), node(6)).  => [6]

                3.  _travese(None, node(5)) ...X
                4.  _travese(None, node(1)) ...X

      5. _travese(node(-1), node(9)) => [6]

                  6. _travese(None, node(5)) ...X
                  7. _travese(node(8), node(8)) =>[6,8]

                          8.  _travese(None, None) ...X
                          9.  _travese(None, None) ...X
"""


