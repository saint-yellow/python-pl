# 面试 Problem Nr. 04-10: 检查子树

from typing import List

from typing_extensions import TypeAlias

from ds import BinaryNode

TreeNode: TypeAlias = BinaryNode


class Solution:
    def checkSubTree(self, t1: TreeNode, t2: TreeNode) -> bool:
        return self.__method1(t1, t2)

    def __method1(self, t1: TreeNode, t2: TreeNode) -> bool:
        if not t2:
            return True

        if not t1:
            return False

        if t1.val == t2.val:
            return self.__method1(t1.left, t2.left) and self.__method1(
                t1.right, t2.right
            )

        return self.__method1(t1.left, t2) or self.__method1(t1.right, t2)
