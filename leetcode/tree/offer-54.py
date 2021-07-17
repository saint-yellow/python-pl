# 剑指Offer Problem Nr. 54: 二叉搜索树的第k大节点

from typing_extensions import TypeAlias

from ds import BinaryNode

TreeNode: TypeAlias = BinaryNode


class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        return self.__method1(root, k)

    def __method1(self, root: TreeNode, k: int):
        inOrder = TreeNode.inOrderTraversal(root)
        nodeCount = len(inOrder)
        return inOrder[nodeCount - k]
