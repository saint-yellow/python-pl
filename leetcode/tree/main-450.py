# LeetCode Problem Nr. 450: 删除二叉树中的节点

from typing_extensions import TypeAlias

from ..ds import BinaryNode

TreeNode: TypeAlias = BinaryNode


class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        return self.__method1(root, key)

    # 基于递归的解法
    def __method1(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return root

        if root.val == key:
            if not (root.left or root.right):
                root = None
            elif (root.left and not root.right) or (not root.left and root.right):
                child = root.left if root.left else root.right
                root = child
            elif root.left and root.right:
                child = root.right
                while child.left:
                    child = child.left
                child.left = root.left
                root = root.right
        elif key < root.val:
            root.left = self.__method1(root.left, key)
        else:
            root.right = self.__method1(root.right, key)

        return root


if __name__ == "__main__":
    tree = TreeNode.buildTree(
        [5, 2, 6, 1, 4, None, 7, None, None, 3, None, None, None, None, None]
    )
    print("before:", TreeNode.levelOrderTraversalWithLayer(tree))

    s = Solution()
    tree = s.deleteNode(tree, 3)
    print("after:", TreeNode.levelOrderTraversalWithLayer(tree))
