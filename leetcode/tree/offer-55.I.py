# 剑指Offer Problem Nr. 55-I: 二叉树的深度

from typing import List

from typing_extensions import TypeAlias

from ds import BinaryNode

TreeNode: TypeAlias = BinaryNode


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return self.__method1(root)

    def __method1(self, root: TreeNode) -> int:
        if not root:
            return 0

        leftMaxDepth = self.maxDepth(root.left)
        rightMaxDepth = self.maxDepth(root.right)
        return 1 + max(leftMaxDepth, rightMaxDepth)

    def __method2(self, root: TreeNode) -> int:
        queue: List[TreeNode] = []
        if root:
            queue.append(root)

        depth = 0
        while queue:
            depth += 1
            size = len(queue)
            for _ in range(size):
                node: TreeNode = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return depth
