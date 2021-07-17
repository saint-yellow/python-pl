# LeetCode Problem Nr. 559: N叉树的最大深度

from typing import List

from typing_extensions import TypeAlias

from ds import NAryNode

Node: TypeAlias = NAryNode


class Solution:
    def maxDepth(self, root: Node) -> int:
        return self.__method1(root)

    def __method1(self, root: Node) -> int:
        queue: List[Node] = []
        if root:
            queue.append(root)

        depth = 0
        while queue:
            depth += 1
            size = len(queue)
            for _ in range(size):
                node: Node = queue.pop(0)
                if node.children:
                    queue.extend(node.children)
        return depth

    def __method2(self, root: Node) -> int:
        if not root:
            return 0

        depth = 0
        if root.children:
            for c in root.children:
                depth = max(depth, self.__method2(c))
        return depth + 1
