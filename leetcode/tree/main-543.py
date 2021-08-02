# LeetCode 主站 Problem Nr. 543: 二叉树的直径

from typing_extensions import TypeAlias

from ..ds import BinaryNode

TreeNode: TypeAlias = BinaryNode


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        return self.__method1(root)

    def __method1(self, root: TreeNode) -> int:
        if not root:
            return 0

        rootDiameter = self.__maxDepth(root.left) + self.__maxDepth(root.right)
        leftDiameter = self.__method1(root.left)
        rightDiameter = self.__method1(root.right)
        return max(rootDiameter, leftDiameter, rightDiameter)

    def __maxDepth(self, root: TreeNode) -> int:
        # 空二叉树
        if root is None:
            return 0

        leftDepth = self.__maxDepth(root.left)
        rightDepth = self.__maxDepth(root.right)

        # 一棵二叉树的最大深度 = 子树的最大深度 + 1
        # 1代表根节点的深度
        return max(leftDepth, rightDepth) + 1
