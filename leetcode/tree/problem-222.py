# LeetCode Problem Nr. 222: 完全二叉树的节点个数

from typing import List

from typing_extensions import TypeAlias

from ds import BinaryNode

TreeNode: TypeAlias = BinaryNode


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        return self.__method1(root)

    # 层序遍历
    def __method1(self, root) -> int:
        queue: List[TreeNode] = []
        if root:
            queue.append(root)

        count = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                node = queue.pop(0)
                count += 1
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return count

    # 深度优先遍历
    def __method2(self, root: TreeNode) -> int:
        if not root:
            return 0

        leftNodes = self.__method2(root.left)
        rightNodes = self.__method2(root.right)
        return 1 + leftNodes + rightNodes

    # 利用完全二叉树的特性
    def __method3(self, root: TreeNode) -> int:
        if not root:
            return 0

        left: TreeNode = root.left
        right: TreeNode = root.right
        leftHeight, rightHeight = 0, 0
        while left:
            left = left.left
            leftHeight += 1
        while right:
            right = right.right
            rightHeight += 1
        if leftHeight == rightHeight:
            # 相当于
            #   return 2 ** (leftHeight + 1) - 1
            return (2 << leftHeight) - 1
        else:
            leftNodes = self.__method3(root.left)
            rightNodes = self.__method3(root.right)
            return leftNodes + rightNodes + 1
