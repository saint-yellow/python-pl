# LeetCode Problem Nr. 109: 有序链表转换二叉搜索树

from typing import List

from typing_extensions import TypeAlias

from ..ds import BinaryNode, SinglyLinkedNode

TreeNode: TypeAlias = BinaryNode
ListNode: TypeAlias = SinglyLinkedNode


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        return self.__method1(head)

    def __method1(self, head: ListNode) -> TreeNode:
        values = self.__listValues(head)
        root = self.__buildBST(values)
        return root

    def __listValues(self, head: ListNode) -> List[int]:
        result: List[int] = []
        while head:
            result.append(head.val)
            head = head.next
        return result

    def __buildBST(self, values: List[int]) -> TreeNode:
        if not values:
            return None

        index = len(values) // 2
        value = values[index]
        root = TreeNode(value)
        root.left = self.__buildBST(values[:index])
        root.right = self.__buildBST(values[index + 1 :])
        return root
