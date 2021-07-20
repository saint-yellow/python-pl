# LeetCode Problem Nr. 513: 找树左下角的值

from typing import List

from typing_extensions import TypeAlias

from ds import BinaryNode

TreeNode: TypeAlias = BinaryNode


class Solution:
    def findBottomLetValue(self, root: TreeNode) -> int:
        return self.__method1(root)

    def __method1(self, root: TreeNode) -> int:
        queue: List[TreeNode] = []
        if root:
            queue.append(root)

        result = 0
        while queue:
            size = len(queue)
            for i in range(size):
                node: TreeNode = queue.pop(0)
                if i == 0:
                    result = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result

    def _method2(self, root: TreeNode) -> int:
        ...
