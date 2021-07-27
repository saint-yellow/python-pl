# LeetCode Problem Nr. 82: 删除排序链表中的重复元素II

from typing_extensions import TypeAlias

from ..ds import SinglyLinkedNode

ListNode: TypeAlias = SinglyLinkedNode


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        return self.__method1(head)

    def __method1(self, head: ListNode) -> ListNode:
        if not head:
            return head

        sentinel = ListNode(-1, head)
        pointer = sentinel
        while pointer.next and pointer.next.next:
            if pointer.next.val == pointer.next.next.val:
                x = pointer.next.val
                while pointer.next and pointer.next.val == x:
                    pointer.next = pointer.next.next
            else:
                pointer = pointer.next
        return sentinel.next


if __name__ == "__main__":
    head = SinglyLinkedNode.buildList([1, 2, 3, 3, 4, 4, 5])
    print(SinglyLinkedNode.listAllValues(head))
    s = Solution()
    print(SinglyLinkedNode.listAllValues(s.deleteDuplicates(head)))
