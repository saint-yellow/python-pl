# LeetCode Problem Nr. 235: 二叉搜索树的最近公共祖先

from typing_extensions import TypeAlias

from ..ds import BinaryNode

TreeNode: TypeAlias = BinaryNode


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        return self.__method1(root, p, q)

    def __method1(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or root == p or root == q:
            return root

        left = self.__method1(root.left, p, q)
        right = self.__method1(root.right, p, q)

        if left and right:
            return root
        if left and not right:
            return left
        if not left and right:
            return right
        return None
