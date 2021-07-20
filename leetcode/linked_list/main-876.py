from typing_extensions import TypeAlias

from ds import SinglyLinkedNode

ListNode: TypeAlias = SinglyLinkedNode


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        return self.__method1(head)

    def __method1(self, head: ListNode) -> ListNode:
        fast, slow = head, head

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        if fast.next is None:
            return slow
        else:
            return slow.next
