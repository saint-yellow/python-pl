from ds import ListNode


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        return self.__method3(head)


    def __method1(self, head: ListNode) -> bool:
        values = []
        current_node = head
        while current_node is not None:
            values.append(current_node.val)
            current_node = current_node.next
        return values == values[::-1]

    
    def __method2(self, head: ListNode) -> bool:
        self.front_pointer = head
        def recursively_check(current_node: ListNode):
            if current_node is not None:
                if not recursively_check(current_node.next):
                    return False
                if self.front_pointer.val != current_node.val:
                    return False
                self.front_pointer = self.front_pointer.next
            return True

        return recursively_check(head)

    def __method3(self, head: ListNode) -> bool:
        if head is None:
            return True

        # 找到前半部分链表的尾节点并反转后半部分链表
        first_half_end = self.__end_of_first_half(head)
        second_half_start = self.__reverse_list(first_half_end.next)

        # 判断是否回文
        result = True
        first_position = head
        second_position = second_half_start
        while result and second_position is not None:
            if first_position.val != second_position.val:
                result = False
            first_position = first_position.next
            second_position = second_position.next

        # 还原链表并返回结果
        first_half_end.next = self.__reverse_list(second_half_start)
        return result    

    def __end_of_first_half(self, head):
        fast = head
        slow = head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow

    def __reverse_list(self, head):
        previous = None
        current = head
        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        return previous
