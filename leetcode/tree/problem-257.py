# LeetCode Problem Nr. 257: 二叉树的所有路径

from typing import List

from typing_extensions import TypeAlias

from ds import BinaryNode
from tree.ds import nodes

TreeNode: TypeAlias = BinaryNode


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        return self.__method2(root)

    def __method1(self, root: TreeNode) -> List[str]:
        result: List[str] = []
        if not root:
            return result

        path: List[int] = []
        self.__traversal(root, path, result)
        return result

    def __traversal(self, node: TreeNode, path: List[int], result: List[str]) -> None:
        path.append(node.val)

        if not (node.left or node.right):
            sPath = ""
            for v in path[0:-1]:
                sPath += f"{v}->"
            sPath += str(path[-1])
            result.append(sPath)
            return

        if node.left:
            self.__traversal(node.left, path, result)
            path.pop()

        if node.right:
            self.__traversal(node.right, path, result)
            path.pop()

    def __method2(self, root: TreeNode) -> List[str]:
        nodeSet: List[TreeNode] = []
        pathSet: List[str] = []
        result: List[str] = []

        if not root:
            return result

        nodeSet.append(root)
        pathSet.append(str(root.val))
        while nodeSet:
            node = nodeSet.pop(0)
            path = pathSet.pop(0)
            if not (node.left or node.right):
                result.append(path)
            if node.right:
                nodeSet.append(node.right)
                pathSet.append(f"{path}->{node.right.val}")
            if node.left:
                nodeSet.append(node.left)
                pathSet.append(f"{path}->{node.left.val}")
        return result
