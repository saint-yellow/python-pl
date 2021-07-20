# LeetCode Problem Nr. 113: 路径总和II

from typing import List

from typing_extensions import TypeAlias

from ds import BinaryNode

TreeNode: TypeAlias = BinaryNode


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        return self.__method1(root, targetSum)

    def __method1(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        ...

    def __method1(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        ...
