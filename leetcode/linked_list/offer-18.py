# 剑指Offer Problem Nr. 18: 删除节点的链表

from typing_extensions import TypeAlias

from ds import SinglyLinkedNode, buildSinglyLinkedList, listAllValues

ListNode: TypeAlias = SinglyLinkedNode


class Solution:
    def deleteNode(self, head: ListNode, value: int) -> ListNode:
        return self.__method1(head, value)

    def __method1(self, head: ListNode, value: int) -> ListNode:
        sentinel = ListNode(-1, head)
        pointer = sentinel
        while pointer.next:
            if pointer.next.val == value:
                pointer.next = pointer.next.next
                return sentinel.next
            else:
                pointer = pointer.next
        return sentinel.next


if __name__ == "__main__":
    linkedList = buildSinglyLinkedList([4, 5, 1, 9])
    s = Solution()
    print(listAllValues(s.deleteNode(linkedList, 4)))
