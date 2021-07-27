# LeetCode Problem Nr. 111: 二叉树的最小深度

from typing import List

from typing_extensions import TypeAlias

from ..ds import BinaryNode

TreeNode: TypeAlias = BinaryNode


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        return self.__method1(root)

    # 递归
    def __method1(self, root: TreeNode) -> int:
        if not root:
            return 0

        leftDepth = self.__method1(root.left)
        rightDepth = self.__method1(root.right)

        if root.left and not root.right:
            return 1 + leftDepth

        if not root.left and root.right:
            return 1 + rightDepth

        return 1 + min(leftDepth, rightDepth)

    # 迭代
    def __method2(self, root: TreeNode) -> int:
        queue: List[TreeNode] = []
        if root:
            queue.append(root)

        depth = 0
        while queue:
            depth += 1
            size = len(queue)
            for _ in range(size):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if not (node.left or node.right):
                    return depth
        return depth
