# LeetCode Problem Nr. 19: 删除链表的倒数第N个结点

from typing_extensions import TypeAlias

from ds import SinglyLinkedNode

ListNode: TypeAlias = SinglyLinkedNode


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        return self.__method1(head, n)

    # 遍历两次
    def __method1(self, head: ListNode, n: int) -> ListNode:
        L = self.__getLength(head)
        sentinel = ListNode(-1, head)
        current = sentinel
        for _ in range(1, L + 1 - n):
            current = current.next
        current.next = current.next.next
        return sentinel.next

    def __getLength(self, head: ListNode) -> int:
        count = 0
        while head is not None:
            count += 1
            head = head.next
        return count

    # 栈
    def __method2(self, head: ListNode, n: int) -> ListNode:
        sentinel = ListNode(-1, head)
        current = sentinel
        stack = []
        while current:
            stack.append(current)
            current = current.next
        for _ in range(n):
            stack.pop()
        node = stack.pop()
        node.next = node.next.next
        return sentinel.next

    # 双指针
    def __method3(self, head: ListNode, n: int) -> ListNode:
        sentinel = ListNode(-1, head)
        slow = sentinel
        fast = sentinel.next
        for _ in range(n):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return sentinel.next
