from typing_extensions import TypeAlias

from ..ds import SinglyLinkedNode

ListNode: TypeAlias = SinglyLinkedNode


class Solution:
    def deleteNode(self, node: ListNode) -> None:
        """
        Do not return anything, modify node in-place instead.
        """

        node.value = node.next.value
        node.next = node.next.next
