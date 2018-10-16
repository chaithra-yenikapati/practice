class Node:
    def __init__(self, val = None):
        self.val = val
        self.left = None
        self.right = None
class Tree:
    def __init__(self):
        self.root = Node(1)
        self.root.right = Node(2)
        self.root.right.left = Node(3)

    def inorderTraversal(self, node, res):
        if not res:
            res = []
        if node:
            res = self.inorderTraversal(node.left, res)
            res.append(node.val)
            res = self.inorderTraversal(node.right, res)
        return res

    def preorderTraversal(self, node, res):
        if not res:
            res = []
        if node:
            res.append(node.val)
            res = self.preorderTraversal(node.left, res)
            res = self.preorderTraversal(node.right, res)
        return res

    def postorderTraversal(self, node, res):
        if not res:
            res = []
        if node:
            res = self.postorderTraversal(node.left, res)
            res = self.postorderTraversal(node.right, res)
            res.append(node.val)
        return res

    

if __name__ == "__main__":
    """
     1 
       \
         2
        /
       3
    """
    t = Tree()
    print(t.inorderTraversal(t.root, []))
    print(t.preorderTraversal(t.root, []))
    print(t.postorderTraversal(t.root, []))
   