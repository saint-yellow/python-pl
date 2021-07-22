# LeetCode Problem Nr. 98: 验证二叉搜索树

from typing import List

from typing_extensions import TypeAlias

from ds import BinaryNode

TreeNode: TypeAlias = BinaryNode


class Solution:
    def __init__(self) -> None:
        self.previousNode: TreeNode = None

    def isValidBST(self, root: TreeNode) -> bool:
        return self.__method1(root)

    # 基于中序遍历的解法

    def __method1(self, root: TreeNode) -> bool:
        inOrder = self.__inOrderTravesal(root)
        if not inOrder:
            return True

        n = len(inOrder)
        if n == 1:
            return True

        for i in range(n - 1):
            if inOrder[i] >= inOrder[i + 1]:
                return False
        return True

    # 二叉搜索树的中序遍历序列有序且单调递增
    def __inOrderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        return (
            self.__inOrderTraversal(root.left)
            + [root.val]
            + self.__inOrderTraversal(root.right)
        )

    def __method2(self, root: TreeNode) -> bool:
        if not root:
            return True

        checkLeft = self.__method2(root.left)
        if self.previousNode and self.previousNode.val >= root.val:
            return False
        self.previousNode = root

        checkRight = self.__method2(root.right)

        return checkLeft and checkRight

    def __method3(self, root: TreeNode) -> bool:
        stack: List[TreeNode] = []
        currentNode: TreeNode = root
        previousNode: TreeNode = None

        while currentNode or stack:
            if currentNode:
                stack.append(currentNode)
                currentNode = currentNode.left
            else:
                currentNode = stack.pop()
                if previousNode and currentNode.val <= previousNode.val:
                    return False
                previousNode = currentNode
                currentNode = currentNode.right
        return True


if __name__ == "__main__":
    tree = TreeNode(0, TreeNode(-1))

    s = Solution()
    print(s.isValidBST(tree))
