# Do not modify the classes below
class TreeNode:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self, representation: str):
        '''
        representation: list of values representing a binary tree. The left and right
        children of the ith element are 2i+1 and 2i+2, respectively.
        '''
        if not representation:
            return
        nodes = []
        for i, value in enumerate(representation):
            node = None
            if value is not None:
                node = TreeNode(value)
                if i > 0:
                    if i % 2 == 1:
                        parent = nodes[(i - 1) // 2]
                        parent.left = node
                    else:
                        parent = nodes[(i - 2) // 2]
                        parent.right = node
            nodes.append(node)
        self.root = nodes[0]


class GraphNode:
    def __init__(self, value=None):
        self.value = value
        self.adjacent = []


class Graph:
    def __init__(self, adjacency: list[list[bool]]):
        '''
        adjacency: list of values representing a binary tree. The left and right
        children of the ith element are 2i+1 and 2i+2, respectively.
        '''
        self.nodes = [GraphNode(i) for i in range(1, len(adjacency) + 1)]
        for node1, row in zip(self.nodes, adjacency):
            for node2, adjacent in zip(self.nodes, row):
                if adjacent and node1 is not node2:
                    node1.adjacent.append(node2)


# Implement the functions below

def pre_order_recursive(root: TreeNode) -> None:
    print(root.value)
    if (root.left is None) and (root.right is None):
        return
    if (root.left is not None): pre_order_recursive(root.left)
    if (root.right is not None): pre_order_recursive(root.right)
    pass

def pre_order_iterative(root: TreeNode) -> None:
    stack = []
    stack.append(root)
    while (len(stack) > 0):
        root = stack.pop()
        if root: print(root.value)
        if (root.right is not None): stack.append(root.right)
        if (root.left is not None): stack.append(root.left)    

def in_order_recursive(root: TreeNode) -> None: 
    if (root.left is not None): in_order_recursive(root.left)
    print(root.value)
    if (root.right is not None): in_order_recursive(root.right)
    if (root.left is None) and (root.right is None):
        return
    pass

def post_order_recursive(root: TreeNode) -> None: 
    if (root.left is not None): post_order_recursive(root.left)
    if (root.right is not None): post_order_recursive(root.right)
    print(root.value)
    if (root.left is None) and (root.right is None):
        return   
    pass


def breadth_first(root: TreeNode) -> None:
    queue = []
    visited = []
    queue.append(root)
    visited.append(root)
    while (len(queue) > 0):
        node = queue.pop(0)
        if node: print(node.value)
        if node.left: 
            visited.append(node.left)
            queue.append(node.left)
        if node.right: 
            visited.append(node.right)
            queue.append(node.right)
    pass


def graph_depth_first_recursive(node: GraphNode, visited=None) -> None:
    if visited is None:
        visited = set()
    # Your code goes here


def graph_depth_first_iterative(node: GraphNode) -> None:
    pass


def graph_breadth_first(node: GraphNode) -> None:
    pas
