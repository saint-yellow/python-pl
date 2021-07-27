# LeetCode Problem Nr. 707: 设计链表

from typing import List

from typing_extensions import TypeAlias

from ..ds import SinglyLinkedNode

ListNode: TypeAlias = SinglyLinkedNode


class MyLinkedList:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 0
        self.sentinel = ListNode(-1, None)

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. \n
        If the index is invalid, return -1.
        """
        if index >= self.size:
            return -1

        node = self.sentinel.next
        for _ in range(index):
            node = node.next
        return node.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. \n
        After the insertion, the new node will be the first node of the linked list.
        """
        oldHead = self.sentinel.next
        newHead = ListNode(val, oldHead)
        self.sentinel.next = newHead
        self.size += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        node = self.sentinel
        for _ in range(self.size):
            node = node.next
        node.next = ListNode(val, None)
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. \n
        If index equals to the length of linked list, the node will be appended to the end of linked list. \n
        If index is greater than the length, the node will not be inserted.
        """
        node1 = self.sentinel
        node2 = self.sentinel.next
        for _ in range(index):
            node1 = node1.next
            node2 = node2.next
        node1.next = ListNode(val, node2)
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index >= self.size:
            return
        node1 = self.sentinel
        node2 = self.sentinel.next
        for _ in range(index):
            node1 = node1.next
            node2 = node2.next
        node1.next = node2.next
        node2.next = None
        self.size -= 1

    def listAllValues(self) -> List[int]:
        result = []
        node = self.sentinel.next
        while node:
            result.append(node.val)
            node = node.next
        return result


if __name__ == "__main__":
    linkedList = MyLinkedList()
    print(linkedList.listAllValues())

    print(linkedList.get(0))

    linkedList.addAtHead(1)
    print(linkedList.listAllValues())

    linkedList.addAtTail(3)
    print(linkedList.listAllValues())

    linkedList.addAtIndex(1, 2)
    print(linkedList.listAllValues())

    linkedList.addAtTail(3)
    print(linkedList.listAllValues())

    linkedList.deleteAtIndex(2)
    print(linkedList.listAllValues())

    linkedList.deleteAtIndex(2)
    print(linkedList.listAllValues())
