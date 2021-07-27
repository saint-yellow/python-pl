# LeetCode Problem Nr. 25: 合并两个排序的链表

from typing_extensions import TypeAlias

from ..ds import SinglyLinkedNode

ListNode: TypeAlias = SinglyLinkedNode


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        return self.__method1(l1, l2)

    def __method1(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        l3: ListNode = ListNode(-1)
        head = l3
        while l1 and l2:
            if l1.val <= l2.val:
                l3.next = l1
                l1 = l1.next
            else:
                l3.next = l2
                l2 = l2.next
            l3 = l3.next

        if l1:
            l3.next = l1
        if l2:
            l3.next = l2

        return head.next
