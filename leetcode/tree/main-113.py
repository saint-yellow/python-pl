# LeetCode Problem Nr. 113: 路径总和II

from typing import List

from typing_extensions import TypeAlias

from ..ds import BinaryNode

TreeNode: TypeAlias = BinaryNode


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        return self.__method1(root, targetSum)

    def __method1(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        result: List[List[int]] = []
        path: List[int] = []

        def dfs(root: TreeNode, targetSum: int) -> None:
            if not root:
                return

            path.append(root.val)
            targetSum -= root.val
            if not root.left and not root.right and targetSum == 0:
                result.append(path[:])
            dfs(root.left, targetSum)
            dfs(root.right, targetSum)
            path.pop()

        dfs(root, targetSum)
        return result

    def __method2(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        ...


if __name__ == "__main__":
    tree = TreeNode(
        5,
        TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))),
        TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(5), TreeNode(1))),
    )

    s = Solution()
    print(s.pathSum(tree, 22))
