from ds import ListNode


class Solution:
    def deleteNode(self, node: ListNode):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """

        node.value = node.next.value
        node.next = node.next.next
