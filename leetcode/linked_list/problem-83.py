class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        return self.method1(head)


    def method1(self, head: ListNode) -> ListNode:
        currentNode = head
        while currentNode is not None and currentNode.next is not None:
            if currentNode.val == currentNode.next.val:
                currentNode.next = currentNode.next.next
            else:
                currentNode = currentNode.next
        return head
