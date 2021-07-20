# LeetCode Problem Nr. 100: 相同的树

from typing_extensions import TypeAlias

from ds import BinaryNode

TreeNode: TypeAlias = BinaryNode


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        return self.__method1(p, q)

    def __method1(self, p: TreeNode, q: TreeNode) -> bool:
        if not (p or q):
            return True
        if not (p and q):
            return False
        if p.val != q.val:
            return False

        comapreLeftTree = self.__method1(p.left, q.left)
        comapreRightTree = self.__method1(p.right, q.right)
        return comapreLeftTree and comapreRightTree
