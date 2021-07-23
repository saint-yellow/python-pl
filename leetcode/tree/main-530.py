# LeetCode Problem Nr. 530: 二叉树的最小绝对差

from typing import List

from typing_extensions import TypeAlias

from ds import BinaryNode

TreeNode: TypeAlias = BinaryNode


class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        return self.__method1(root)

    def __method1(self, root: TreeNode) -> int:
        inOrder = self.__inOrderTraversal(root)
        minDiff = abs(inOrder[1] - inOrder[0])
        n = len(inOrder)
        for i in range(1, n - 1):
            if minDiff > abs(inOrder[i + 1] - inOrder[i]):
                minDiff = abs(inOrder[i + 1] - inOrder[i])
        return minDiff

    def __inOrderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        return (
            self.__inOrderTraversal(root.left)
            + [root.val]
            + self.__inOrderTraversal(root.right)
        )


if __name__ == "__main__":
    tree = TreeNode.buildTree([4, 2, 6, 1, 3, None, None])
    print(TreeNode.inOrderTraversal(tree))
    s = Solution()
    print(s.getMinimumDifference(tree))
