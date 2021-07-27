# 程序员面试金典 Problem Nr. 04.03: 特定深度节点链表

from typing import List

from typing_extensions import TypeAlias

from ds import BinaryNode, SinglyLinkedNode

TreeNode: TypeAlias = BinaryNode
ListNode: TypeAlias = SinglyLinkedNode


class Solution:
    def listOfDepth(self, tree: TreeNode) -> List[ListNode]:
        return self.__method1(tree)

    def __method1(self, tree: TreeNode) -> List[ListNode]:
        queue: List[TreeNode] = []
        if tree:
            queue.append(tree)

        result: List[ListNode] = []
        while queue:
            size = len(queue)
            sentinel = ListNode(-1)
            pointer = sentinel
            for _ in range(size):
                node = queue.pop(0)
                pointer.next = ListNode(node.val)
                pointer = pointer.next

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(sentinel.next)
        return result
