class Treenode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)


class Tree:
    def __init__(self, root):
        self.root = root

    def preorder_traverse(self, node=None):
        if node is None:
            node = self.root
        print(node.value)
        for child in node.children:
            self.preorder_traverse(child)

    def postorder_traverse(self, node=None):
        if node is None:
            node = self.root
        for child in node.children:
            self.postorder_traverse(child)
        print(node.value)


# Build the tree
t = Tree(Treenode("A"))

# Add children to root
b = Treenode("B")
c = Treenode("C")
d = Treenode("D")

t.root.add_child(b)
t.root.add_child(c)
t.root.add_child(d)

# Add children to B
b.add_child(Treenode("E"))
b.add_child(Treenode("F"))

# Add child to C
c.add_child(Treenode("G"))

# Traversals
print("Preorder:")
t.preorder_traverse()

print("\nPostorder:")
t.postorder_traverse()
