# LeetCode Problem Nr. 112: 路径总和

from ds import TreeNode


class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        return self.__method1(root, targetSum)

    def __method1(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False

        if not root.left and not root.right:
            return targetSum == root.val

        left = self.__method1(root.left, targetSum-root.val) 
        right = self.__method1(root.right, targetSum-root.val)
        return left or right

    def __method2(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False

        nodeQueue = [root]
        valueQueue = [root.val]

        while nodeQueue:
            length = len(nodeQueue)
            for _ in range(length):
                node = nodeQueue.pop(0)
                value = valueQueue.pop(0)
                if not node.left and not node.right:
                    if value == targetSum:
                        return True
                if node.left:
                    nodeQueue.append(node.left)
                    valueQueue.append(value+node.left.val)
                if node.right:
                    nodeQueue.append(node.right)
                    valueQueue.append(value+node.right.val)
        return False
            
        