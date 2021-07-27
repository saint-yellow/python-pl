# LeetCode Problem Nr. 671: 二叉树中第二小的节点

from typing import List

from typing_extensions import TypeAlias

from ds import BinaryNode

TreeNode: TypeAlias = BinaryNode


class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        return self.__method1(root)

    # 遍历全树再排序取其第二小者，退而求其次的解法
    def __method1(self, root: TreeNode) -> int:
        preOrder = self.__preOrderTraversal(root)
        preOrder.sort()
        firstMinimumValue = preOrder[0]
        for n in preOrder[1:]:
           if n > firstMinimumValue:
               return n
        return -1

    def __preOrderTraversal(self, root: TreeNode) -> List[int]:
        stack: List[TreeNode] = []

        if root:
            stack.append(root)

        result: List[int] = []

        while stack:
            node = stack.pop()
            if node:
                if node.right:
                    stack.append(node.right)

                if node.left:
                    stack.append(node.left)

                stack.append(node)
                stack.append(None)
            else:
                node = stack.pop()
                result.append(node.val)

        return result

    


if __name__ == '__main__':
    tree1 = TreeNode.buildTree([2, 2, 5, None, None, 5, 7])
    tree2 = TreeNode.buildTree([2, 2, 2])

    s = Solution()
    print(s.findSecondMinimumValue(tree1))
    print(s.findSecondMinimumValue(tree2))
