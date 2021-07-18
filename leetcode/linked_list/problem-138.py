# LeetCode Problem Nr. 138: 复制带随机指针的链表

from typing import Dict, List, Union

from ds import SinglyLinkedNode


class Node(SinglyLinkedNode):
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val: int = x
        self.next: Node = next
        self.random: Node = random


class Solution:
    def copyRandomList(self, head: Node) -> Node:
        return self.__method1(head)

    def __method1(self, head: Node) -> Node:
        hasMap: Dict[Node, Node] = {}
        pointer = head

        while pointer:
            hasMap[pointer] = Node(pointer.val)
            pointer = pointer.next

        pointer = head
        while pointer:
            node = hasMap.get(pointer, None)
            node.next = hasMap.get(pointer.next, None)
            node.random = hasMap.get(pointer.random, None)
            pointer = pointer.next

        return hasMap(head, None)

    def __method2(self, head: Node) -> Node:
        ...

    def __method3(self, head: Node) -> Node:
        ...

    def __method4(self, head: Node) -> Node:
        ...
