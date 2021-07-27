# LeetCode Problem Nr. 1382: 将二叉搜索树变平衡

from typing import List

from typing_extensions import TypeAlias

from ..ds import BinaryNode

TreeNode: TypeAlias = BinaryNode


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        return self.__method1(root)

    def __method1(self, root: TreeNode) -> TreeNode:
        inOrder = self.__inOrderTraversal(root)
        n = len(inOrder)
        if n < 3:
            return root

        return self.__buildBST(inOrder)

    def __inOrderTraversal(self, root: TreeNode) -> List[TreeNode]:
        if not root:
            return []

        left, right = root.left, root.right
        root.left, root.right = None, None
        return (
            self.__inOrderTraversal(left) +
            [root] +
            self.__inOrderTraversal(right)
        )

    def __buildBST(self, nodes: List[TreeNode]) -> TreeNode:
        if not nodes:
            return None

        middleIndex = len(nodes) // 2
        root = nodes[middleIndex]
        root.left = self.__buildBST(nodes[:middleIndex])
        root.right = self.__buildBST(nodes[middleIndex+1:])
        return root

    def __isBalanced(self, root: TreeNode) -> bool:
        ...


if __name__ == '__main__':
    numbers = [None] * 15
    numbers[0], numbers[2], numbers[6], numbers[14] = 1, 2, 3, 4
    tree = TreeNode.buildTree(numbers)

    s = Solution()
    s.balanceBST(tree)
