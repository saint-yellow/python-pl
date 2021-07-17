# LeetCode Problem Nr. 144: 二叉树的前序遍历

from typing import List

from typing_extensions import TypeAlias

from ds import BinaryNode

TreeNode: TypeAlias = BinaryNode


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        return self.__method3(root)

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

    def __method3(self, root: TreeNode) -> List[int]:
        result: List[int] = []
        stack: List[TreeNode] = []

        if root:
            stack.append(root)

        while stack:
            node: TreeNode = stack[-1]
            if node:
                stack.pop()             
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)

                stack.append(node)
                stack.append(None)
            else:
                stack.pop()

                node = stack[-1]
                result.append(node.value)
                stack.pop()
        return result


if __name__ == '__main__':
    s = Solution()
    tree = TreeNode(1, None, TreeNode(2, TreeNode(3), None))
    print(s.preorderTraversal(tree))
