# LeetCode Problem Nr. 145: 二叉树的后序遍历

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        return self.__method1(root)


    # 递归
    def __method1(self, root: TreeNode) -> List[int]:
        if root:
            return self.__method1(root.left) + self.__method1(root.right) + [root.val]
        else:
            return []