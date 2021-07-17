# LeetCode Problem Nr. 111: 二叉树的最小深度

from typing_extensions import TypeAlias

from ds import BinaryNode

TreeNode: TypeAlias = BinaryNode


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        return self.__method2(root)

    # 自顶向下的解法
    def __method1(self, node: TreeNode, depth: int) -> int: ...

    # 自底向上的解法
    def __method2(self, node: TreeNode) -> int: ...
