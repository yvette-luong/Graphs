class GraphNode:
    def __init__(self, value):
        self.value = value
        self.edge = []
    
a = GraphNode(7)
b = GraphNode(3)
c = GraphNode(1)
d = GraphNode(6)
e = GraphNode(9)

a.edge = [b, e] # a goes to be, and a goes to e 
b.edge = [c, d]

'''

    def pre_order(n):
    if n is None:
        return
    print(n.value) # "visit" the node
    pre_order(n.left)  # then visit the left neighbor
    pre_order(n.right)  # then visit the right neighbor

'''

def dft(n):
    # visit the node
    print(n.value)
    # visit all the neighbors
    for e in n.edges:
        dft(e)
    
dft(a)