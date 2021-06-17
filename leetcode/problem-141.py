class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        return self.method1(head)

    def method1(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False

        slow = head
        fast = slow.next
        while slow != fast:
            slow = slow.next
            try:
                fast = fast.next.next
                if fast is None:
                    return False
            except:
                return False
        return True
