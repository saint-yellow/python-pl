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
    def preOrderTraversal(root: "BinaryNode", fillWithNone: bool = False) -> List[int]:
        if not root:
            return [None] if fillWithNone else []
        return (
            [root.val]
            + BinaryNode.preOrderTraversal(root.left, fillWithNone)
            + BinaryNode.preOrderTraversal(root.right, fillWithNone)
        )

    # 中序遍历
    @staticmethod
    def inOrderTraversal(root: "BinaryNode", fillWithNone: bool = False) -> List[int]:
        if not root:
            return [None] if fillWithNone else []
        return (
            BinaryNode.inOrderTraversal(root.left, fillWithNone)
            + [root.val]
            + BinaryNode.preOrderTraversal(root.right, fillWithNone)
        )

    # 后序遍历
    @staticmethod
    def postOrderTraversal(root: "BinaryNode", fillWithNone: bool = False) -> List[int]:
        if not root:
            return [None] if fillWithNone else []
        return (
            BinaryNode.postOrderTraversal(root.left, fillWithNone)
            + BinaryNode.postOrderTraversal(root.right, fillWithNone)
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
    def buildTree(values: List[Union[int, None]]) -> "BinaryNode":
        if not values:
            return None

        nodes: List[Union[BinaryNode, None]] = [
            None if not v else BinaryNode(v) for v in values
        ]
        lastIndex = len(values) - 1
        fatherCount = lastIndex // 2 - 1
        for i in range(fatherCount + 1):
            if nodes[i]:
                nodes[i].left = nodes[2 * i + 1]
                nodes[i].right = nodes[2 * i + 2]
        return nodes[0]


class NAryNode:
    def __init__(self, val: int = 0, children: List["NAryNode"] = None) -> None:
        self.val = val
        self.children: List["NAryNode"] = children
