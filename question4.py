# Find the least common ancestor between two nodes on
# a binary search tree. The least common ancestor is
# the farthest node from the root that is an ancestor
# of both nodes. For example, the root is a common ancestor
# of all nodes on the tree, but if both nodes are descendents
# of the root's left child, then that left child might be
# the lowest common ancestor. You can assume that both nodes
# are in the tree, and the tree itself adheres to all
# BST properties. The function definition should look
# like question4(T, r, n1, n2), where T is the tree represented
# as a matrix, where the index of the list is equal to the integer
# stored in that node and a 1 represents a child node, r is a
# non-negative integer representing the root, and n1 and n2 are
# non-negative integers representing the two nodes in no particular
# order. For example, one test case might be

# question4([[0, 1, 0, 0, 0],
#           [0, 0, 0, 0, 0],
#           [0, 0, 0, 0, 0],
#           [1, 0, 0, 0, 1],
#           [0, 0, 0, 0, 0]],
#          3,
#          1,
#          4)
# and the answer would be 3.

# BST node
class Node(object):
    # Creates a new node
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Finds lowest common ancestor (LCA)
def lca(root, n1, n2):
# Base case
    if root is None:
        return None
    while root is not None:

        # Check to see if n1 and n2 are smaler than the root
        # if so put to left of root and if bigger put to right
        # else, return the root value
        if (root.value > n1 and root.value > n2):
            return lca(root.left, n1, n2)
        elif (root.value < n1 and root.value < n2):
            return lca(root.right, n1, n2)
        else:
            return root.value
    return root

# This function adds new node to right or left
# depending if new value is higher than root or lower
def new_node(node, new_value):
    if (node != None):
        if (new_value <= node.value):
            new_node = Node(new_value)
            node.left = new_node
            return new_node
        else:
            new_node = Node(new_value)
            node.right = new_node
            return new_node
        return None

def question4(T, r, n1, n2):
    node_val = 0
    root = Node(r)
    length = len(T)
    l_list = []

    if length == 0:
        return T
    elif len(T) == 1:
        return r

    if T is not None:
        for i in T[r]:
            if node_val < length:
                l_list.append(new_node(root, node_val))
        node_val += 1

        tmp_node = l_list.pop(0)
        while tmp_node != None:

            node_val = 0
            for i in T[tmp_node.value]:
                if node_val > tmp_node.value:
                    l_list.append(new_node(tmp_node, node_val))
            node_val += 1

            return lca(root, n1, n2)
        return None
    return None


print question4([[0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [1, 0, 0, 0, 1],
           [0, 0, 0, 0, 0]],
          3,
          1,
          4)

print question4([[0]],
                0,
                0,
                0)

print question4([[0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 1, 0, 1, 0, 0],
                 [1, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 1, 0, 0, 1],
                 [0, 0, 0, 0, 0, 0, 0]],
                1,
                0,
                6)

print question4([],
                None,
                None,
                None)

# Time complexity: The solution goes through the ancestors of n1 and n2
# and takes the LCA from that list so the time complexity will be O(n)