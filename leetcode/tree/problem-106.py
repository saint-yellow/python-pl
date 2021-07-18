# LeetCode Problem Nr. 106: 从中序与后序遍历序列构造二叉树

from typing import List

from typing_extensions import TypeAlias

from ds import BinaryNode

TreeNode: TypeAlias = BinaryNode


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        return self.__method1(inorder, postorder)

    def __method1(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        mapper = {value: index for (index, value) in enumerate(inorder)}

        def helper(leftIndex: int, rightIndex: int) -> TreeNode:
            if leftIndex > rightIndex:
                return None

            value = postorder.pop()
            index = mapper[value]
            root = TreeNode(value, None, None)
            root.right = helper(index + 1, rightIndex)
            root.left = helper(leftIndex, index - 1)
            return root

        return helper(0, len(inorder) - 1)

    def __method2(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        pass
