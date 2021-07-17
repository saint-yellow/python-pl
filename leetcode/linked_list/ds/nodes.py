from typing import List


# Definition for singly-linked list.
class SinglyLinkedNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class DoublyLinkedNode:
    def __init__(self, val: int, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


def buildSinglyLinkedList(values: List[int]):
    if not values:
        return None

    node = SinglyLinkedNode(-1)
    head = node
    for i in values:
        node.next = SinglyLinkedNode(i, None)
        node = node.next
    return head.next


def listAllValues(head: SinglyLinkedNode) -> List[int]:
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result
