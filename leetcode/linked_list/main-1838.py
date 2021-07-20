# LeetCode Problem Nr. 1838: 旋转链表

from typing_extensions import TypeAlias

from ds import SinglyLinkedNode, buildSinglyLinkedList, listAllValues

ListNode: TypeAlias = SinglyLinkedNode


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        return self.__method1(head, k)

    def __method1(self, head: ListNode, k: int) -> ListNode:
        if not (head and head.next):
            return head

        n = 1
        tail = head
        while tail.next:
            tail = tail.next
            n += 1
        tail.next = head

        step = n - k % n - 1
        pointer = head
        for _ in range(step):
            pointer = pointer.next
        newHead = pointer.next
        pointer.next = None
        return newHead


if __name__ == "__main__":
    s = Solution()
    for k in range(1, 6):
        linkedList = buildSinglyLinkedList([1, 2, 3, 4, 5, 6, 7, 8])
        print(listAllValues(s.rotateRight(linkedList, k)))
