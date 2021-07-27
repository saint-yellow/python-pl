# 剑指Offer Nr. 26: 树的子结构

from typing_extensions import TypeAlias

from ..ds import BinaryNode

TreeNode: TypeAlias = BinaryNode


class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        return self.__method1(A, B)

    def __method1(self, A: TreeNode, B: TreeNode) -> bool:
        if not A or not B:
            return False

        return (
            self.__isContain(A, B)
            or self.__method1(A.left, B)
            or self.__method1(A.right, B)
        )

    def __isContain(self, A: TreeNode, B: TreeNode) -> bool:
        if not B:
            return True

        if not A or A.val != B.val:
            return False

        return self.__isContain(A.left, B.left) and self.__isContain(A.right, B.right)
