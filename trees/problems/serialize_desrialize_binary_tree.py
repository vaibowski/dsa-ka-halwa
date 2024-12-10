class Codec:

    def __init__(self):
        self.i = None

    def serialize(self, root):
        if not root:
            return 'x'

        return str(root.val) + "," + self.serialize(root.left) + "," + self.serialize(root.right)

    def deserialize(self, data):
        nodes = data.split(",")
        self.i = 0

        def dfs():
            if self.i == len(nodes):
                return None

            nodeVal = nodes[self.i]
            self.i += 1

            if nodeVal == "x":
                return None

            root = TreeNode(int(nodeVal))
            root.left = dfs()
            root.right = dfs()
            return root

        return dfs()
