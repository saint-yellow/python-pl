# LeetCode Problem Nr. 101: 对称的二叉树

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.method2(root)

    # 递归
    def method1(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        return p.val == q.val and self.method1(p.left, q.right) and self.method1(p.right, q.left)

    # 迭代
    def method2(self, root: TreeNode) -> bool:
        node1, node2 = root, root
        queue = [node1, node2]
        while len(queue) > 0:
            node1 = queue.pop(0)
            node2 = queue.pop(0)
            if not node1 and not node2:
                continue
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
            queue.append(node1.left)
            queue.append(node2.right)
            queue.append(node1.right)
            queue.append(node2.left)
        return True

