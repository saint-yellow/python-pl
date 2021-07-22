# LeetCode Problem Nr. 112: 路径总和

from typing import List, Tuple

from typing_extensions import TypeAlias

from ds import BinaryNode

TreeNode: TypeAlias = BinaryNode


class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        return self.__method1(root, targetSum)

    def __method1(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False

        if not root.left and not root.right:
            return targetSum == root.val

        left = self.__method1(root.left, targetSum - root.val)
        right = self.__method1(root.right, targetSum - root.val)
        return left or right

    def __method2(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False

        nodeQueue = [root]
        # valueQueue = [root.val]

        while nodeQueue:
            length = len(nodeQueue)
            for _ in range(length):
                node = nodeQueue.pop(0)
                # value = valueQueue.pop(0)
                if not node.left and not node.right:
                    if node.val == targetSum:
                        return True
                if node.left:
                    nodeQueue.append(node.left)
                    # valueQueue.append(value + node.left.val)
                if node.right:
                    nodeQueue.append(node.right)
                    # valueQueue.append(value + node.right.val)
        return False

    def __method3(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False

        return self.__traversal(root, targetSum - root.val)

    def __traversal(self, node: TreeNode, count: int) -> bool:
        if not (node.left or node.right):
            if count == 0:
                return True
            else:
                return False

        if node.left:
            count -= node.left.val
            if self.__traversal(node.left, count):
                return True
            count += node.left.val

        if node.right:
            count -= node.right.val
            if self.__traversal(node.right, count):
                return True
            count += node.right.val

        return False

    def __method4(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False

        stack: List[Tuple[TreeNode, int]] = [(root, root.val)]
        while stack:
            (node, value) = stack.pop()

            if not (node.left or node.right) and targetSum == value:
                return True

            if node.right:
                stack.append((node.right, value + node.right.val))

            if node.left:
                stack.append((node.left, value + node.left.val))

        return False
