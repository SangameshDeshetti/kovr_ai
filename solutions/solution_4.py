# ToDo: Edge cases and exception handling
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    # Your function signature should be:
    def preorder_traversal(self, root, preorder_list=[]) -> list:
        if not root:
            return []
        preorder_list.append(root.val)
        self.preorder_traversal(root.left)
        self.preorder_traversal(root.right)
        return preorder_list


if __name__ == '__main__':
    root = TreeNode(1)
    node1 = TreeNode(2)
    node2 = TreeNode(3)
    root.left = node1
    root.right = node2
    node3 = TreeNode(4)
    node4 = TreeNode(5)
    node1.left = node3
    node1.right = node4
    node5 = TreeNode(6)
    node6 = TreeNode(7)
    node2.left = node5
    node2.right = node6
    print(root.preorder_traversal(root=root))
