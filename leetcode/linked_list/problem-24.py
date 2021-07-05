# LeetCode problem #24: 反转链表


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        return self.__method1(head)

    # 基于双指针的迭代法
    def __method1(self, head: ListNode) -> ListNode:
        slow: ListNode = None
        fast: ListNode = head
        while fast:
            temp: ListNode = fast.next
            fast.next = slow
            slow = fast
            fast = temp
        return slow

    # 递归法
    def __method2(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        ret: ListNode = self.__method2(head.next)
        head.next.next = head
        head.next = None
        return ret

    def __method3(self, head: ListNode) -> ListNode:
        pass
