# Name: William Clements 
# OSU Email: clementsw@oregeonstate.edu
# Course: CS261 - Data Structures
# Assignment:3, Part 2
# Due Date: 7/24/2023 (Note: Taking 2 free days on this assignment)
# Description: Stack ADT class


from DynamicArray import DynamicArray

class StackException(Exception):
    """Custom exception to be used by Stack class."""
    pass

class DynamicArrayStack:
    def __init__(self):
        """Initialize new stack based on Dynamic Array."""
        self._da = DynamicArray()

    def __str__(self):
        """Override string method to provide more readable output."""
        size = self._da.length()
        out = "STACK: " + str(size) + " element(s). ["
        for i in range(size - 1):
            out += str(self._da[i]) + ', '
        if size > 0:
            out += str(self._da[size - 1])
        return out + ']'

    def is_empty(self):
        """Return True if the stack is empty, False otherwise."""
        return self._da.is_empty()

    def size(self):
        """Return number of elements currently in the stack."""
        return self._da.length()

    def push(self, value):
        """Add a new value to the top of the stack."""
        self._da.append(value)

    def pop(self):
        """Remove and return the value from the top of the stack.
        If the stack is empty, raise a custom 'StackException'."""
        if self.is_empty():
            raise StackException("Stack is empty")
        return self._da.pop()

    def top(self):
        """Return the value from the top of the stack without removing it.
        If the stack is empty, raise a custom 'StackException'."""
        if self.is_empty():
            raise StackException("Stack is empty")
        return self._da[self._da.length() - 1]