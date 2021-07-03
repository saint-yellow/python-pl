# LeetCode Problem Nr. 144: 二叉树的前序遍历

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        return self.method1(root)


    # 递归
    def method1(self, root: TreeNode) -> List[int]:
        if root:
            return [root.value] + self.method1(root.left) + self.method1(root.right)
        else:
            return []
