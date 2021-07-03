class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.deque = []
        self.capacity = k
        

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if len(self.deque) >= self.capacity:
            return False
        self.deque.insert(0, value)
        return True
        
        

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if len(self.deque) >= self.capacity:
            return False
        self.deque.append(value)
        return True
        

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        try:
            del self.deque[0]
            return True
        except:
            return False
        

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        try:
            del self.deque[-1]
            return True
        except:
            return False
        
        

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if not self.deque:
            return -1
        else:
            return self.deque[0]
        

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if not self.deque:
            return -1
        else:
            return self.deque[-1]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return len(self.deque) == 0
        

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return len(self.deque) == self.capacity