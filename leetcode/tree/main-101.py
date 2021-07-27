# LeetCode Problem Nr. 101: 对称的二叉树

from typing import List

from typing_extensions import TypeAlias

from ..ds import BinaryNode

TreeNode: TypeAlias = BinaryNode


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.__method2(root)

    # 递归
    def __method1(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        return (
            p.val == q.val
            and self.__method1(p.left, q.right)
            and self.__method1(p.right, q.left)
        )

    # 迭代
    def __method2(self, root: TreeNode) -> bool:
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

    # 层次遍历
    def __method3(self, root: TreeNode) -> bool:
        queue: List[TreeNode] = []
        if root:
            queue.append(root)

        while queue:
            size = len(queue)
            values = []
            for _ in range(size):
                node = queue.pop(0)
                if node:
                    values.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    values.append(None)
            if values != values[::-1]:
                return False
        return True
