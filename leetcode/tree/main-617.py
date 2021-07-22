# LeetCode Problem Nr. 617: 合并二叉树

from typing import List

from typing_extensions import TypeAlias

from ds import BinaryNode

TreeNode: TypeAlias = BinaryNode


class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        return self.__method1(root1, root2)

    def __method1(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not root1:
            return root2

        if not root2:
            return root1

        root1.val += root2.val
        root1.left = self.__method1(root1.left, root2.left)
        root1.right = self.__method1(root1.right, root2.right)
        return root1

    def __method2(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not root1:
            return root2

        if not root2:
            return root1

        queue: List[TreeNode] = [root1, root2]
        while queue:
            node1 = queue.pop(0)
            node2 = queue.pop(0)
            
            node1.val += node2.val

            if not (node1.left or node2.left):
                queue.append(node1.left)
                queue.append(node2.left)

            if not (node1.right or node2.right):
                queue.append(node1.right)
                queue.append(node2.right)

            if not node1.left and node2.left:
                node1.left = node2.left

            if not node1.right and node2.right:
                node1.right = node2.right

        return root1
