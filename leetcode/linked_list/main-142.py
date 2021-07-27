from typing_extensions import TypeAlias

from ..ds import SinglyLinkedNode

ListNode: TypeAlias = SinglyLinkedNode


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        return self.__method1(head)

    def __method1(self, head: ListNode) -> ListNode:
        fast, slow = head, head

        while True:
            if not (fast and fast.next):
                return None
            fast, slow = fast.next.next, slow.next
            if fast == slow:
                break

        fast = head
        while fast != slow:
            fast, slow = fast.next, slow.next

        return fast
