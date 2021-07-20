# LeetCode Problem Nr. 106: 从前序与后序遍历序列构造二叉树

from typing import List

from typing_extensions import TypeAlias

from ds import BinaryNode

TreeNode: TypeAlias = BinaryNode


class Solution:
    def buildTree(self, preOrder: List[int], inOrder: List[int]) -> TreeNode:
        return self.__method1(preOrder, inOrder)

    def __method1(self, preOrder: List[int], inOrder: List[int]) -> TreeNode:
        mapper = {value: index for (index, value) in enumerate(inOrder)}

        def helper(leftIndex: int, rightIndex: int) -> TreeNode:
            if leftIndex > rightIndex:
                return None

            value = preOrder.pop(0)
            index = mapper[value]
            root = TreeNode(value, None, None)
            root.left = helper(leftIndex, index - 1)
            root.right = helper(index + 1, rightIndex)
            return root

        return helper(0, len(inOrder) - 1)

    def __method2(self, preOrder: List[int], inOrder: List[int]) -> TreeNode:
        if not preOrder:
            return None

        rootValue = preOrder.pop()
        root = TreeNode(rootValue)

        if len(preOrder) == 1:
            return root

        delimiterIndex = 0
        while delimiterIndex < len(inOrder):
            if inOrder[delimiterIndex] == rootValue:
                break
            delimiterIndex += 1

        root.left = self.__method2(preOrder[1:delimiterIndex+1], inOrder[0:delimiterIndex])
        root.right = self.__method2(preOrder[delimiterIndex+1:], inOrder[delimiterIndex+1:])

        return root
