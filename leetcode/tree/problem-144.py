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
        return self.__method2(root)


    # 递归
    def __method1(self, root: TreeNode) -> List[int]:
        if root:
            return [root.value] + self.__method1(root.left) + self.__method1(root.right)
        else:
            return []

    # 迭代
    def __method2(self, root: TreeNode) -> List[int]:
        result = []
        if not root:
            return result

        stack = [root]
        while stack:
            node = stack.pop()
            result.append(node.value)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result


if __name__ == '__main__':
    s = Solution()
    tree = TreeNode(1, None, TreeNode(2, TreeNode(3), None))
    print(s.preorderTraversal(tree))
