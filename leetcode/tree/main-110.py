# LeetCode Problem Nr. 110: 平衡二叉树

from typing_extensions import TypeAlias

from ds import BinaryNode

TreeNode: TypeAlias = BinaryNode


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.__method1(root)

    def __method1(self, root: TreeNode) -> bool:
        if self.__getHeight(root) == -1:
            return False
        return True

    def __getHeight(self, root: TreeNode) -> int:
        if not root:
            return 0

        leftHeight = self.__getHeight(root.left)
        if leftHeight == -1:
            return -1
        rightHeight = self.__getHeight(root.right)
        if rightHeight == -1:
            return -1

        if abs(leftHeight - rightHeight) > 1:
            return -1
        else:
            return 1 + max(leftHeight, rightHeight)
