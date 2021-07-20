from typing import List


# Definition for a binary tree node.
class BinaryNode:
    def __init__(self, val: int = 0, left: 'BinaryNode' = None, right: 'BinaryNode' = None):
        self.val: int = val
        self.left: BinaryNode = left
        self.right: BinaryNode = right

    @staticmethod
    def preOrderTraversal(root: 'BinaryNode') -> List[int]:
        if not root:
            return []
        return (
            [root.val]
            + BinaryNode.preOrderTraversal(root.left)
            + BinaryNode.preOrderTraversal(root.right)
        )

    @staticmethod
    def inOrderTraversal(root: 'BinaryNode') -> List[int]:
        if not root:
            return []
        return (
            BinaryNode.inOrderTraversal(root.left)
            + [root.val]
            + BinaryNode.preOrderTraversal(root.right)
        )

    @staticmethod
    def postOrderTraversal(root: 'BinaryNode') -> List[int]:
        if not root:
            return []
        return (
            BinaryNode.postOrderTraversal(root.left)
            + BinaryNode.postOrderTraversal(root.right)
            + [root.val]
        )


def buildTree(values: List[int]) -> BinaryNode:
    ...


def listAllValues(root: BinaryNode) -> List[int]:
    ...


class NAryNode:
    def __init__(self, val: int = 0, children: List['NAryNode'] = None):
        self.val = val
        self.children: List['NAryNode'] = children
