# LeetCode Problem Nr. 55-II: 平衡二叉树

from typing_extensions import TypeAlias

from ds import BinaryNode

TreeNode: TypeAlias = BinaryNode


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.__method1(root)

    def __method1(self, root: TreeNode) -> bool:
        if not root:
            return True

        leftDepth = self.__getDepth(root.left)
        rightDepth = self.__getDepth(root.right)
        if abs(leftDepth - rightDepth) > 1:
            return False

        checkLeftTree = self.__method1(root.left)
        checkRightTree = self.__method1(root.right)
        return checkLeftTree and checkRightTree
        
    def __getDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        leftDepth = self.__getDepth(root.left)
        rightDepth = self.__getDepth(root.right)
        return 1 + max(leftDepth, rightDepth)


if __name__ == '__main__':
    tree = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))), TreeNode(2, None, TreeNode(3, None, TreeNode(4))))

    s = Solution()
    print(s.isBalanced(tree))
