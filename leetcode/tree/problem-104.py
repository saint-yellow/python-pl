# LeetCode Problem Nr. 104: 二叉树的最大深度

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return self.__method2(root)


    # 自顶向下的解法
    def __method1(self, node: TreeNode, depth: int) -> int:
        '''
        node: 当前遍历到的节点
        depth: 遍历到当前节点前所算得的最大深度
        '''

        # 空节点
        if node is None:
            return depth

        # 叶子节点
        if node.left is None and node.right is None:
            return depth+1

        # 计算左、右两子树的最大深度，并取其最大者
        leftDepth = self.__method1(node.left, depth+1)
        rightDepth = self.__method1(node.right, depth+1)
        return max(leftDepth, rightDepth)

    # 自底向上的解法
    def __method2(self, node: TreeNode) -> int:
        # 空二叉树
        if node is None:
            return 0

        leftDepth = self.__method2(node.left)
        rightDepth = self.__method2(node.right)

        # 一棵二叉树的最大深度 = 子树的最大深度 + 1 
        # 1代表根节点的深度
        return max(leftDepth, rightDepth) + 1

