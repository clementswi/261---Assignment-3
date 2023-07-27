# Name: William Clements
# OSU Email: clementsw@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 3, Part 3
# Due Date: 7/24/2023 (Note: Taking 2 free days on this assignment)
# Description: Queue ADT class


from static_array import StaticArray

class QueueException(Exception):
    """Custom exception to be used by Queue class."""
    pass

class Queue:
    def __init__(self) -> None:
        """Initialize new queue based on Static Array."""
        self._sa = StaticArray(4)
        self._front = 0
        self._back = -1
        self._current_size = 0

    def __str__(self) -> str:
        """Override string method to provide more readable output."""
        size = self._current_size
        out = "QUEUE: " + str(size) + " element(s). ["

        front_index = self._front
        for _ in range(size - 1):
            out += str(self._sa[front_index]) + ', '
            front_index = self._increment(front_index)
        if size > 0:
            out += str(self._sa[front_index])

        return out + ']'

    def is_empty(self) -> bool:
        """Return True if the queue is empty, False otherwise."""
        return self._current_size == 0

    def size(self) -> int:
        """Return number of elements currently in the queue."""
        return self._current_size

    def _increment(self, index: int) -> int:
        """Move index to the next position with wraparound."""
        index += 1
        if index == self._sa.length():
            index = 0
        return index

# ---------------------------------------------------------------------- #

    def enqueue(self, value: object) -> None:
        """Add an element to the back of the queue."""
        if self._current_size == self._sa.length():
            self._double_queue()

        self._back = self._increment(self._back)
        self._sa[self._back] = value
        self._current_size += 1

    def dequeue(self) -> object:
        """Remove and return the front element of the queue."""
        if self.is_empty():
            raise QueueException("Queue is empty, cannot dequeue.")

        front_value = self._sa[self._front]
        self._front = self._increment(self._front)
        self._current_size -= 1
        return front_value

    def front(self) -> object:
        """Return the front element of the queue without removing it."""
        if self.is_empty():
            raise QueueException("Queue is empty, cannot get front.")

        return self._sa[self._front]

    def _double_queue(self) -> None:
        """Resize the queue by doubling its capacity."""
        new_capacity = self._sa.length() * 2
        new_sa = StaticArray(new_capacity)

        front_index = self._front
        for i in range(self._current_size):
            new_sa[i] = self._sa[front_index]
            front_index = self._increment(front_index)

        self._sa = new_sa
        self._front = 0
        self._back = self._current_size - 1