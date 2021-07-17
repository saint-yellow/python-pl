# LeetCode Problem Nr. 106: 从前序与后序遍历序列构造二叉树

from typing import List

from typing_extensions import TypeAlias

from ds import BinaryNode

TreeNode: TypeAlias = BinaryNode


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        return self.__method1(preorder, inorder)

    def __method1(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        mapper = {value: index for (index, value) in enumerate(inorder)}

        def helper(leftIndex: int, rightIndex: int) -> TreeNode:
            if leftIndex > rightIndex:
                return None

            value = preorder.pop(0)
            index = mapper[value]
            root = TreeNode(value, None, None)
            root.left = helper(leftIndex, index-1)
            root.right = helper(index+1, rightIndex)
            return root

        return helper(0, len(inorder)-1)

    def __method2(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        pass
