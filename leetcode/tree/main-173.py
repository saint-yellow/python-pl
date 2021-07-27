# LeetCode Problem Nr. 173: 二叉搜索树迭代器

from typing import List

from typing_extensions import TypeAlias

from ds import BinaryNode

TreeNode: TypeAlias = BinaryNode


class BSTIterator:
    def __init__(self, root: TreeNode) -> None:
        self.nodes: List[int] = self.__inOrderTravesal(root)

    def next(self) -> int:
        value = self.nodes[0]
        self.nodes = self.nodes[1:]
        return value

    def hasNext(self) -> bool:
        return len(self.nodes) > 0

    def __inOrderTravesal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        return (
            self.__inOrderTravesal(root.left)
            + [root.val]
            + self.__inOrderTravesal(root.right)
        )
