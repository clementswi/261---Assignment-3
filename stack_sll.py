# Name:William Clements
# OSU Email: clementsw@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 3, Part 4
# Due Date: 7/24/2023 (Note: Taking 2 free days on this assignment)
# Description:Stack ADT class


from SLNode import SLNode


class StackException(Exception):
    """Custom exception to be used by Stack class"""
    pass


class Stack:
    def __init__(self) -> None:
        """Initialize new stack with head node"""
        self._head = None

    def __str__(self) -> str:
        """Return content of stack in human-readable form"""
        out = 'STACK ['
        if not self.is_empty():
            node = self._head
            out = out + str(node.value)
            node = node.next
            while node:
                out = out + ' -> ' + str(node.value)
                node = node.next
        return out + ']'

    def is_empty(self) -> bool:
        """Return True is the stack is empty, False otherwise"""
        return self._head is None

    def size(self) -> int:
        """Return number of elements currently in the stack"""
        node = self._head
        length = 0
        while node:
            length += 1
            node = node.next
        return length

    def push(self, value: object) -> None:
        """Add a new element to the top of the stack"""
        new_node = SLNode(value)
        new_node.next = self._head
        self._head = new_node

    def pop(self) -> object:
        """Remove and return the top element from the stack"""
        if self.is_empty():
            raise StackException("Stack is empty, cannot perform pop operation.")

        top_value = self._head.value
        self._head = self._head.next
        return top_value

    def top(self) -> object:
        """Return the top element of the stack without removing it"""
        if self.is_empty():
            raise StackException("Stack is empty, cannot perform top operation.")

        return self._head.value