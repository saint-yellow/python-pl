# LeetCode Problem Nr. 106: 从中序与后序遍历序列构造二叉树

from typing import List

from typing_extensions import TypeAlias

from ds import BinaryNode

TreeNode: TypeAlias = BinaryNode


class Solution:
    def buildTree(self, inOrder: List[int], postOrder: List[int]) -> TreeNode:
        return self.__method1(inOrder, postOrder)

    def __method1(self, inOrder: List[int], postOrder: List[int]) -> TreeNode:
        mapper = {value: index for (index, value) in enumerate(inOrder)}

        def helper(leftIndex: int, rightIndex: int) -> TreeNode:
            if leftIndex > rightIndex:
                return None

            value = postOrder.pop()
            index = mapper[value]
            root = TreeNode(value, None, None)
            root.right = helper(index + 1, rightIndex)
            root.left = helper(leftIndex, index - 1)
            return root

        return helper(0, len(inOrder) - 1)

    def __method2(self, inOrder: List[int], postOrder: List[int]) -> TreeNode:
        if not postOrder:
            return None

        rootValue = postOrder[-1]
        root = TreeNode(rootValue)

        if len(postOrder) == 1:
            return root

        delimiterIndex = 0
        while delimiterIndex < len(inOrder):
            if inOrder[delimiterIndex] == rootValue:
                break
            delimiterIndex += 1

        root.left = self.__method2(inOrder[:delimiterIndex], postOrder[:delimiterIndex+1])
        root.right = self.__method2(inOrder[delimiterIndex+1:], postOrder[delimiterIndex:-1])

        return root
