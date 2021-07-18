# LeetCode Problem Nr. 203: 移除链表元素

from typing_extensions import TypeAlias

from ds import SinglyLinkedNode, buildSinglyLinkedList, listAllValues

ListNode: TypeAlias = SinglyLinkedNode


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        return self.__method1(head, val)

    def __method1(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return None

        start = ListNode(-1, head)
        pointer = start
        while pointer and pointer.next:
            if pointer.next.val == val:
                pointer.next = pointer.next.next
            else:
                pointer = pointer.next
        return start.next


if __name__ == "__main__":
    s = Solution()
    head = buildSinglyLinkedList([6, 6, 6, 6])
    value = 6
    print(listAllValues(head))
    print(listAllValues(s.removeElements(head, value)))
