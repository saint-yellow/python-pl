# 剑指Offer Problem Nr. 52: 两个链表的第一个公共节点

from typing_extensions import TypeAlias

from ..ds import SinglyLinkedNode

ListNode: TypeAlias = SinglyLinkedNode


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        return self.__method2(headA, headB)

    # 基于哈希集合的解法
    def __method1(self, headA: ListNode, headB: ListNode) -> ListNode:
        nodes = set()
        while headA:
            nodes.add(headA)
            headA = headA.next

        while headB:
            if headB in nodes:
                return headB
            headB = headB.next
        return None

    # 基于双指针的解法
    def __method2(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None

        pointerA, pointerB = headA, headB
        while pointerA != pointerB:
            pointerA = headB if not pointerA else pointerA.next
            pointerB = headA if not pointerB else pointerB.next
        return pointerA
