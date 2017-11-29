# Given an undirected graph G,
# find the minimum spanning tree within G.
# A minimum spanning tree connects all vertices
# in a graph with the smallest possible total
# weight of edges. Your function should take in
# and return an adjacency list structured like this:

'''
{'A': [('B', 2)],
 'B': [('A', 2), ('C', 5)],
 'C': [('B', 5)]}
'''
# Vertices are represented as unique strings.
# The function definition should be question3(G)

def question3(G):
    # made for runtime errors
    if len(G) < 1:
        return G
    # make sure G is dictionary
    if type(G) != dict:
        return "Error: G is not dictionary!"

    # Create key for graph G
    vertices = set(G.keys())
    min_span_tree = {}
    # Sets starting point for graph
    start = G.keys()[0]
    # creates a starting point of the graph
    min_span_tree[start] = []

    while len(min_span_tree.keys()) < len(vertices):
        # all other vertices are initialized to infinity
        min_weight = float('inf')
        min_edge = None
        for vertex in min_span_tree.keys():
            for (node, weight) in G[vertex]:
                if node not in min_span_tree.keys():
                    edges = (weight, node)
                if len(edges) > 0:
                    w, v = edges
                if w < min_weight:
                    min_weight = w
                    min_edge = (vertex, v)
        min_span_tree[min_edge[0]].append((min_edge[1], min_weight))
        min_span_tree[min_edge[1]] = [(min_edge[0], min_weight)]
    return min_span_tree

# Efficiency: O(n*m) due to the fact of edges and vertices are each visited once in the while loop.

# Code design: I chose Prim's algorithm which at each step will
# choose the cheapest route to the next step. In this case,
# the cheapest next step is the edge with the lowest weight.
# I used a boolean array (min_span_tree) to represent the set of
# vertices included in the MST. If a value min_span_tree[v] is true,
# then vertex v is included in MST, otherwise not.

print question3({'A': [('B', 3), ('E', 1)],
                 'B': [('A', 3), ('C', 9), ('D', 2), ('E', 2)],
                 'C': [('B', 9), ('D', 3), ('E', 7)],
                 'D': [('B', 2), ('C', 3)],
                 'E': [('A', 1), ('B', 2), ('C', 7)]})
