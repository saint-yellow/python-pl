# LeetCode Problem Nr. 94: 二叉树的中序遍历

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        return self.method1(root)

    # 递归
    def method1(self, root: TreeNode) -> List[int]:
        if root is not None:
            return self.method1(root.left) + [root.value] + self.method1(root.right)
        else:
            return []

    # 迭代
    def method2(self, root: TreeNode) -> List[int]:
        pass

    # 莫里斯遍历
    def method2(self, root: TreeNode) -> List[int]:
        pass

