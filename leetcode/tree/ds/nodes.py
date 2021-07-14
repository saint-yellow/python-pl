from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left=None, right=None):
        self.val: int = val
        self.left = left
        self.right = right

    @staticmethod
    def preOrderTraversal(root) -> List[int]:
        if not root:
            return []
        return [root.val] + TreeNode.preOrderTraversal(root.left) + TreeNode.preOrderTraversal(root.right)

    @staticmethod
    def inOrderTraversal(root) -> List[int]:
        if not root:
            return []
        return TreeNode.inOrderTraversal(root.left) + [root.val] + TreeNode.preOrderTraversal(root.right)

    @staticmethod
    def postOrderTraversal(root) -> List[int]:
        if not root:
            return []
        return TreeNode.postOrderTraversal(root.left) + TreeNode.postOrderTraversal(root.right) + [root.val]


def buildTree(values: List[int]) -> TreeNode: ...
def listAllValues(root: TreeNode) -> List[int]: ...
