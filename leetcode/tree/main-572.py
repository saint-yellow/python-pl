# LeetCode Problem Nr. 572: 另一棵树的子树

from ..ds import BinaryNode
from typing_extensions import TypeAlias

TreeNode: TypeAlias = BinaryNode


class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        return self.__method1(root, subRoot)

    def __method1(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if not root:
            return False

        if root.val == subRoot.val and self.__isSameTree(root, subRoot):
            return True

        return self.__method1(root.left, subRoot) or self.__method1(root.right, subRoot)

    def __isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not (p or q):
            return True
        if not (p and q):
            return False
        if p.val != q.val:
            return False

        comapreLeftTree = self.__isSameTree(p.left, q.left)
        comapreRightTree = self.__isSameTree(p.right, q.right)
        return comapreLeftTree and comapreRightTree
