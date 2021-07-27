from typing_extensions import TypeAlias

from ..ds import SinglyLinkedNode

ListNode: TypeAlias = SinglyLinkedNode


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        return self.__method2(head)

    # 基于迭代的解法
    def __method1(self, head: ListNode) -> ListNode:
        previousNode = None
        while head is not None:
            nextNode = head.next
            head.next = previousNode
            previousNode = head
            head = nextNode
        return previousNode

    # 基于递归的解法
    def __method2(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        else:
            nextHead = self.__method2(head.next)
            head.next.next = head
            head.next = None
            return nextHead
