# LeetCode Problem Nr. 1609: 奇偶树

from typing import List

from ds import TreeNode


class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        return self.__method1(root)

    def __method1(self, root: TreeNode) -> bool:
        queue: List[TreeNode] = []
        if root:
            queue.append(root)
        
        level = 0
        while queue:
            levelSize = len(queue)
            numbers: List[int] = []
            for _ in range(levelSize):
                node: TreeNode = queue.pop(0)
                numbers.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if not self.__checkLevel(numbers, level):
                return False
            level += 1
        return True

    def __checkLevel(self, numbers: List[int], level: int) -> bool:
        evenOrOdd = (level+1) % 2
        for n in numbers:
            if n % 2 != evenOrOdd:
                return False
            
        n = len(numbers)
        if evenOrOdd == 1:
            for i in range(1, n):
                if numbers[i] <= numbers[i-1]:
                    return False
        else:
            for i in range(1, n):
                if numbers[i] >= numbers[i-1]:
                    return False
        return True


if __name__ == '__main__':
    tree = TreeNode(5, TreeNode(9, TreeNode(3, None), TreeNode(5, None)), TreeNode(1, TreeNode(7, None, None)))
    s = Solution()
    print(s.isEvenOddTree(tree))
