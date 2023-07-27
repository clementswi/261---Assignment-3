# Name: William Clements 
# OSU Email: clementsw@oregeonstate.edu
# Course: CS261 - Data Structures
# Assignment:3, Part 2
# Due Date: 7/24/2023 (Note: Taking 2 free days on this assignment)
# Description: Stack ADT class


from dynamic_array import DynamicArray


class StackException(Exception):
    """Custom exception to be used by Stack class"""
    pass


class Stack:
    def __init__(self):
        """Initialize new stack with dynamic array"""
        self._da = DynamicArray()

    def __str__(self) -> str:
        """Return content of stack in human-readable form"""
        out = 'STACK ['
        if not self.is_empty():
            node = self._da._head
            out = out + str(node.value)
            node = node.next
            while node:
                out = out + ' -> ' + str(node.value)
                node = node.next
        return out + ']'

    def is_empty(self) -> bool:
        """Return True if the stack is empty, False otherwise"""
        return self._da.is_empty()

    def size(self) -> int:
        """Return number of elements currently in the stack"""
        return self._da.length()

    def push(self, value: object) -> None:
        """Add a new value to the top of the stack"""
        self._da.append(value)

    def pop(self) -> object:
        """Remove and return the value from the top of the stack"""
        if self.is_empty():
            raise StackException("Stack is empty")
        value = self._da[self._da.length() - 1]
        self._da.remove_at_index(self._da.length() - 1)
        return value

    def top(self) -> object:
        """Return the value from the top of the stack without removing it"""
        if self.is_empty():
            raise StackException("Stack is empty")
        return self._da[self._da.length() - 1]