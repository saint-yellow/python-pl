# LeetCode Problem Nr. 86: 分割链表

from typing_extensions import TypeAlias

from ds import SinglyLinkedNode, buildSinglyLinkedList

ListNode: TypeAlias = SinglyLinkedNode


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        return self.__method1(head, x)

    def __method1(self, head: ListNode, x: int) -> ListNode:
        smallHead, largeHead = ListNode(-1), ListNode(-1)
        smallPointer, largePointer = smallHead, largeHead

        while head:
            if head.val < x:
                smallPointer.next = head
                smallPointer = smallPointer.next
            else:
                largePointer.next = head
                largePointer = largePointer.next
            head = head.next
        largePointer.next = None
        smallPointer.next = largeHead.next
        return smallHead.next


if __name__ == "__main__":
    s = Solution()
    list1 = buildSinglyLinkedList([1, 4, 3, 2, 5, 2])
    print(list1.listValues())
    print(s.partition(list1, 3).listValues())
    list2 = ListNode(2, ListNode(1, None))
    print(list2.listValues())
    print(s.partition(list2, 2).listValues())
