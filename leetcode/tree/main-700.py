# LeetCode Problem Nr. 700: 二叉搜索树中的搜索

from typing_extensions import TypeAlias

from ..ds import BinaryNode

TreeNode: TypeAlias = BinaryNode


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        return self.__method1(root, val)

    def __method1(self, root: TreeNode, val: int) -> TreeNode:
        if not root or root.val == val:
            return root
        elif val < root.val:
            return self.__method1(root.left, val)
        else:
            return self.__method1(root.right, val)

    def __method2(self, root: TreeNode, val: int) -> TreeNode:
        while root:
            if root.val == val:
                return root
            elif val < root.val:
                root = root.left
            else:
                root = root.right
        return root
