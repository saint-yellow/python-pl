# 程序员面试金典 Problem Nr. 04.02: 最小高度树

from typing import List

from typing_extensions import TypeAlias

from ..ds import BinaryNode

TreeNode: TypeAlias = BinaryNode


class Solution:
    def sortedArrayToBST(self, numbers: List[int]) -> TreeNode:
        return self.__method1(numbers)

    def __method1(self, numbers: List[int]) -> TreeNode:
        if not numbers:
            return None

        index = len(numbers) // 2
        value = numbers[index]
        root = TreeNode(value)
        root.left = self.__method1(numbers[:index])
        root.right = self.__method1(numbers[index + 1 :])
        return root
