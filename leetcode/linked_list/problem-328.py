# LeetCode Problem Nr. 328: 奇偶链表

from typing_extensions import TypeAlias

from ds import SinglyLinkedNode, buildSinglyLinkedList, listAllValues

ListNode: TypeAlias = SinglyLinkedNode


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        return self.__method1(head)

    def __method1(self, head: ListNode) -> ListNode:
        if not (head and head.next):
            return head

        oddHead, evenHead = head, head.next
        oddPointer, evenPointer = oddHead, evenHead

        while evenPointer and evenPointer.next:
            oddPointer.next = evenPointer.next
            evenPointer.next = oddPointer.next.next
            oddPointer = oddPointer.next
            evenPointer = evenPointer.next

        oddPointer.next = evenHead
        return oddHead


if __name__ == '__main__':
    listHead = buildSinglyLinkedList([2, 1, 3, 5, 6, 4, 7])
    print(listAllValues(listHead))

    s = Solution()
    print(listAllValues(s.oddEvenList(listHead)))
