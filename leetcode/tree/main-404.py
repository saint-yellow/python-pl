# LeetCode Problem Nr. 404: 左叶子之和

from typing import List

from typing_extensions import TypeAlias

from ..ds import BinaryNode

TreeNode: TypeAlias = BinaryNode


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        return self.__method1(root)

    def __method1(self, root: TreeNode) -> int:
        if not root:
            return 0

        leftValue = self.__method1(root.left)
        rightValue = self.__method1(root.right)

        middleValue = 0
        if root.left and not root.left.left and not root.left.right:
            middleValue = root.left.val

        return middleValue + leftValue + rightValue

    def __method2(self, root: TreeNode) -> int:
        queue: List[TreeNode] = []
        if root:
            queue.append(root)

        result = 0
        while queue:
            node: TreeNode = queue.pop(0)
            if node.left and not node.left.left and not node.right.right:
                result += node.left.val
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
        return result
