# LeetCode Problem Nr. 654: 最大二叉树

from typing import List

from typing_extensions import TypeAlias

from ds import BinaryNode

TreeNode: TypeAlias = BinaryNode


class Solution:
    def constructMaximumBinaryTree(self, numbers: List[int]) -> TreeNode:
        return self.__method1(numbers)

    def __method1(self, numbers: List[int]) -> TreeNode:
        if not numbers:
            return None

        maxValue, maxIndex = 0, 0
        for (i, v) in enumerate(numbers):
            if maxValue < v:
                maxIndex, maxValue = i, v

        root = TreeNode(maxValue)
        root.left = self.__method1(numbers[:maxIndex])
        root.right = self.__method1(numbers[maxIndex + 1:])
        return root

    def __method2(self, numbers: List[int]) -> TreeNode:
        return self.__traversal(numbers, 0, len(numbers))
    
    def __traversal(self, numbers: List[int], left: int, right: int) -> TreeNode:
        if left >= right:
            return None

        index = left
        for i in range(left+1, right):
            if numbers[index] < numbers[i]:
                index = i

        root = TreeNode(numbers[index])
        root.left = self.__traversal(numbers, left, index)
        root.right = self.__traversal(numbers, index + 1, right)
        return root
