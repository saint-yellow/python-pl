# LeetCode Problem Nr. 102: 二叉树的层序遍历

from typing import List

from typing_extensions import TypeAlias

from ds import BinaryNode

TreeNode: TypeAlias = BinaryNode


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        return self.__method1(root)

    # 基于广度优先遍历的解法
    def __method1(self, root: TreeNode) -> List[List[int]]:
        result = []
        if not root:
            return result
        queue = [root]
        while queue:
            levelSize = len(queue)
            currentLevel = []
            for _ in range(levelSize):
                node = queue.pop(0)
                currentLevel.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(currentLevel)
        return result

    # 基于广度优先遍历的解法，借助Python的collections模块
    def __method2(self, root: TreeNode) -> List[List[int]]:
        result = []
        if not root:
            return result

        from collections import deque

        queue = deque()
        queue.append(root)

        while queue:
            levelSize = len(queue)
            currentLevel = []
            for _ in range(levelSize):
                node: TreeNode = queue.popleft()
                currentLevel.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(currentLevel)

        return result

    # 基于深度优先遍历的解法
    def __method3(self, root: TreeNode) -> List[List[int]]:
        result: List[List[int]] = []

        def dfs(node: TreeNode, level: int) -> None:
            if not node:
                return
            if len(result) < level + 1:
                result.append([])
            result[level].append(node.val)
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        if not root:
            return result
        dfs(root, 0)
        return result
