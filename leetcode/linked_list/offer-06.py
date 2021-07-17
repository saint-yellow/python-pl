# 剑指Offer Problem Nr. 09: 从尾到头打印链表

from typing import List

from typing_extensions import TypeAlias

from ds import SinglyLinkedNode

ListNode: TypeAlias = SinglyLinkedNode


class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        return self.__method1(head)

    def __method1(self, head: ListNode) -> List[int]:
        if not head:
            return []

        result = []
        while head:
            result.append(head.val)
            head = head.next
        return result[::-1]

    def __method2(self, head: ListNode) -> List[int]:
        if not head:
            return []

        previousNode: ListNode = None
        while head:
            nextNode = head.next
            head.next = previousNode
            head = nextNode
        
        result = []
        while head:
            result.append(head.val)
            head = head.next
        return result[::-1]
