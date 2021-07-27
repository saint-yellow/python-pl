# LeetCode Problem Nr. 701: 二叉搜索树中的插入操作

from typing_extensions import TypeAlias

from ..ds import BinaryNode

TreeNode: TypeAlias = BinaryNode


class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        return self.__method1(root, val)

    def __method1(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)

        if val < root.val:
            root.left = self.__method1(root.left, val)
        if val > root.val:
            root.right = self.__method1(root.right, val)

        return root
