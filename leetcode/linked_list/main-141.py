from typing_extensions import TypeAlias

from ..ds import SinglyLinkedNode

ListNode: TypeAlias = SinglyLinkedNode


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        return self.__method1(head)

    # 基于双指针的解法
    def __method1(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False

        slow = head
        fast = slow.next
        while slow != fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast is None:
                return False
        return True

    # 基于集合的解法
    def __method2(self, head: ListNode) -> bool:
        nodes = set()
        current: ListNode = head
        while current:
            if current in nodes:
                return True
            nodes.add(current)
            current = current.next
        return False
