from typing import List, Union


# Definition for a binary tree node.
class BinaryNode:
    def __init__(
        self, val: int = 0, left: "BinaryNode" = None, right: "BinaryNode" = None
    ):
        self.val: int = val
        self.left: BinaryNode = left
        self.right: BinaryNode = right

    # 前序遍历
    @staticmethod
    def preOrderTraversal(root: "BinaryNode") -> List[int]:
        if not root:
            return []
        return (
            [root.val]
            + BinaryNode.preOrderTraversal(root.left)
            + BinaryNode.preOrderTraversal(root.right)
        )

    # 中序遍历
    @staticmethod
    def inOrderTraversal(root: "BinaryNode") -> List[int]:
        if not root:
            return []
        return (
            BinaryNode.inOrderTraversal(root.left)
            + [root.val]
            + BinaryNode.preOrderTraversal(root.right)
        )

    # 后序遍历
    @staticmethod
    def postOrderTraversal(root: "BinaryNode") -> List[int]:
        if not root:
            return []
        return (
            BinaryNode.postOrderTraversal(root.left)
            + BinaryNode.postOrderTraversal(root.right)
            + [root.val]
        )

    @staticmethod
    def levelOrderTraversalWithLayer(root: "BinaryNode") -> List[List[int]]:
        queue: List[BinaryNode] = []
        if root:
            queue.append(root)

        result: List[List[int]] = []
        while queue:
            size = len(queue)
            layer: List[int] = []
            for _ in range(size):
                node: BinaryNode = queue.pop(0)
                layer.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(layer)
        return result

    @staticmethod
    def levelOrderTraversal(root: "BinaryNode") -> List[int]:
        queue: List[BinaryNode] = []
        if root:
            queue.append(root)

        result: List[int] = []
        while queue:
            size = len(queue)
            for _ in range(size):
                node: BinaryNode = queue.pop(0)
                result.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result

    @staticmethod
    def buildTree(values: List[Union(int, None)]) -> "BinaryNode":
        ...


class NAryNode:
    def __init__(self, val: int = 0, children: List["NAryNode"] = None):
        self.val = val
        self.children: List["NAryNode"] = children


class BinarySearchNode(BinaryNode):
    ...
