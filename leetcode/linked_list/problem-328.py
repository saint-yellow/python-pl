# LeetCode Problem Nr. 328: 奇偶链表

from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def buildList(values: List[int]):
    if not values:
        return None

    node = ListNode(-1)
    head = node
    for i in values:
        node.next = ListNode(i, None)
        node = node.next
    return head.next

def listAllValues(head: ListNode) -> List[int]:
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

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
    listHead = buildList([2,1,3,5,6,4,7])
    print(listAllValues(listHead))

    s = Solution()
    print(listAllValues(s.oddEvenList(listHead)))
