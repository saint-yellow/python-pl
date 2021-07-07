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
        return self.__method3(root)


    # 递归
    def __method1(self, root: TreeNode) -> List[int]:
        if root:
            return self.__method1(root.left) + self.__method1(root.right) + [root.value]
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
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        result.reverse()
        return result

    def __method3(self, root: TreeNode) -> List[int]:
        result: List[int] = []
        stack: List[TreeNode] = []

        if root:
            stack.append(root)

        while stack:
            node: TreeNode = stack[-1]
            if node:
                stack.pop()
                stack.append(node)
                stack.append(None)
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
            else:
                stack.pop()

                node = stack[-1]
                result.append(node.value)
                stack.pop()
                
        return result


if __name__ == '__main__':
    s = Solution()
    tree = TreeNode(1, None, TreeNode(2, TreeNode(3), None))
    print(s.postorderTraversal(tree))
