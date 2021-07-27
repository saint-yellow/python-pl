# LeetCode Problem Nr. 958: 二叉树的完全性检验

from typing import List, Tuple

from typing_extensions import TypeAlias

from ..ds import BinaryNode

TreeNode: TypeAlias = BinaryNode


class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        return self.__method1(root)

    def __method1(self, root: TreeNode) -> bool:
        nodes: List[Tuple[TreeNode, int]] = [(root, 1)]
        i = 0
        while i < len(nodes):
            node, index = nodes[i]
            i += 1
            if node:
                nodes.append((node.left, 2 * index))
                nodes.append((node.right, 2 * index + 1))
        return nodes[-1][1] == len(nodes)


if __name__ == "__main__":
    tree = TreeNode.buildTree([None])

    s = Solution()
    print(s.isCompleteTree(tree))
