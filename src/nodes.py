'''
    Nodes/ Verts/ Vertexes/ 
    are connected by
    Edges 

    Edges can be 
        Directed    one-way    
'''
class ListNode:
    def __init__(self, value):
        self.value = value
        self.next  = None
    
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class GraphNode:
    def __init__(self, value):
        self.value = value
        self.edge = [] 
        
        