# LeetCode Problem Nr. 111: 二叉树的最小深度

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        return self.method2(root)


    # 自顶向下的解法
    def method1(self, node: TreeNode, depth: int) -> int:
        pass

    # 自底向上的解法
    def method2(self, node: TreeNode) -> int:
       pass

