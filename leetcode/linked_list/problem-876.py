class ListNode:
    def __init__(self, x: int) -> None:
        self.val = x
        self.next = None


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        return self.__method1(head)

    def __method1(self, head: ListNode) -> ListNode:
        fast, slow = head, head

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        if fast.next is None:
            return slow
        else:
            return slow.next
