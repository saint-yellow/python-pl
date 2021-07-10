# LeetCode Problem Nr. 86: 分割链表

from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def listValues(self) -> List[int]:
        result = []
        head = self
        while head:
            result.append(head.val)
            head = head.next
        return result


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


if __name__ == '__main__':
    s = Solution()
    list1 = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2, None))))))
    print(list1.listValues())
    print(s.partition(list1, 3).listValues())
    list2 = ListNode(2, ListNode(1, None))
    print(list2.listValues())
    print(s.partition(list2, 2).listValues())

