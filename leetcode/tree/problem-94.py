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
        return self.__method2(root)

    # 递归
    def __method1(self, root: TreeNode) -> List[int]:
        if root is not None:
            return self.__method1(root.left) + [root.value] + self.__method1(root.right)
        else:
            return []

    # 迭代
    def __method2(self, root: TreeNode) -> List[int]:
        result = []
        stack = []
        currentNode = root

        while currentNode or stack:
            if currentNode:
                stack.append(currentNode)
                currentNode = currentNode.left
            else:
                currentNode = stack.pop()
                result.append(currentNode.value)
                currentNode = currentNode.right
                
        return result

    # 莫里斯遍历
    def __method3(self, root: TreeNode) -> List[int]:
        pass



if __name__ == '__main__':
    s = Solution()
    tree = TreeNode(1, None, TreeNode(2, TreeNode(3), None))
    print(s.inorderTraversal(tree))

