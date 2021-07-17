# LeetCode Problem Nr. 28: 二叉树的镜像

from typing import List

from typing_extensions import TypeAlias

from ds import BinaryNode

TreeNode: TypeAlias = BinaryNode


class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        return self.__method1(root)

    def __method1(self, root: TreeNode) -> TreeNode:
        queue: List[TreeNode] = []
        if root:
            queue.append(root)

        while queue:
            size = len(queue)
            for _ in range(size):
                node: TreeNode = queue.pop(0)
                node.left, node.right = node.right, node.left
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root
