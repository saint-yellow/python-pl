# LeetCode Problem Nr. 114: 二叉树展开为链表

from typing import List

from ds import TreeNode


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.__method1(root)


    def __method1(self, root: TreeNode) -> None:
        values = TreeNode.preOrderTraversal(root)
        if not values:
            return
        root.left = None
        root.right = None
        pointer = root
        for v in values[1:]:
            pointer.right = TreeNode(v)
            pointer = pointer.right


    def __method2(self, root: TreeNode) -> None:
        pass

    def __method3(self, root: TreeNode) -> None:
        pass

if __name__ == '__main__':
    tree = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5, None, TreeNode(6)))
    print(TreeNode.preOrderTraversal(tree))

    s = Solution()
    s.flatten(tree)
