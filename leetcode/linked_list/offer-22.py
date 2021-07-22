# 剑指Offer Problem Nr. 22: 链表中倒数第k个节点

from typing_extensions import TypeAlias

from ds import SinglyLinkedNode

ListNode: TypeAlias = SinglyLinkedNode


class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        return self.__method1(head, k)

    def __method1(self, head: ListNode, k: int) -> ListNode:
        slow, fast = head, head
        for _ in range(k):
            fast = fast.next
            if not fast:
                return None
        while fast:
            slow = slow.next
            fast = fast.next
        return slow


if __name__ == "__main__":
    linkedList = SinglyLinkedNode.buildList([1, 2, 3, 4, 5])
    s = Solution()
    print(SinglyLinkedNode.listAllValues(s.getKthFromEnd(linkedList, 2)))
