# LeetCode Problem Nr. 94: 二叉树的中序遍历

from typing import List

from typing_extensions import TypeAlias

from ds import BinaryNode

TreeNode: TypeAlias = BinaryNode


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        return self.__method3(root)

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
                stack.append(node)
                stack.append(None)
                if node.left:
                    stack.append(node.left)
            else:
                stack.pop()

                node = stack[-1]
                result.append(node.value)
                stack.pop()
        return result

    # 莫里斯遍历
    def __method4(self, root: TreeNode) -> List[int]:
        ...


if __name__ == "__main__":
    s = Solution()
    tree = TreeNode(1, None, TreeNode(2, TreeNode(3), None))
    print(s.inorderTraversal(tree))
