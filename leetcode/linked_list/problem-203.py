# LeetCode Problem Nr. 203: 移除链表元素

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


if __name__ == '__main__':
    s = Solution()
    # head = ListNode(1, ListNode(2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6, None)))))))
    head = buildList([6,6,6,6])
    value = 6
    print(listAllValues(head))
    print(listAllValues(s.removeElements(head, value)))
        