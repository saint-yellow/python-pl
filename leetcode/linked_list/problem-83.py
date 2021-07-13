from ds import ListNode


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        return self.__method1(head)


    def __method1(self, head: ListNode) -> ListNode:
        currentNode = head
        while currentNode is not None and currentNode.next is not None:
            if currentNode.val == currentNode.next.val:
                currentNode.next = currentNode.next.next
            else:
                currentNode = currentNode.next
        return head
