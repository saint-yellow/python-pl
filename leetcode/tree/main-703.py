from typing import List


class TreeNode:
    def __init__(
        self, val: int, left: "TreeNode" = None, right: "TreeNode" = None
    ) -> None:
        self.val = val
        self.left = left
        self.right = right
        self.count: int = 1


class KthLargest:
    def __init__(self, k: int, numbers: List[int]):
        self.k = k
        self.tree: TreeNode = None

        for n in numbers:
            self.tree = self.__insertTreeNode(self.tree, n)

    def add(self, val: int) -> int:
        self.tree = self.__insertTreeNode(self.tree, val)
        return self.__getKthLargestNode(self.tree, self.k)

    def __insertTreeNode(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)

        if val < root.val:
            root.left = self.__insertTreeNode(root.left, val)
        else:
            root.right = self.__insertTreeNode(root.right, val)
        root.count += 1

        return root

    def __getKthLargestNode(self, root: TreeNode, k: int) -> int:
        currentCount = 1

        if root.right:
            currentCount += root.right.count

        if k == currentCount:
            return root.val
        elif k < currentCount:
            return self.__getKthLargestNode(root.right, k)
        else:
            return self.__getKthLargestNode(root.left, k - currentCount)
