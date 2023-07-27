# Name: William Clements
# OSU Email: clementsw@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 3, Part 5
# Due Date: 7/24/2023 (Note: 2 free days used on this assignment)
# Description: Queue class

from SLNode import SLNode

class QueueException(Exception):
    """Custom exception to be used by Queue class
DO NOT CHANGE THIS METHOD IN ANY WAY
"""
    pass


class Queue:
    def __init__(self):
        """Initialize new queue with head and tail nodes
        DO NOT CHANGE THIS METHOD IN ANY WAY"""
        self._head = SLNode(None)
        self._tail = None

    def __str__(self):
        """Return content of queue in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY"""
        out = 'QUEUE ['
        if not self.is_empty():
            node = self._head.next
            out = out + str(node.value)
            node = node.next
            while node:
                out = out + ' -> ' + str(node.value)
                node = node.next
        return out + ']'

    def is_empty(self) -> bool:
        """Return True if the queue is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._head.next is None

    def size(self) -> int:
        """Return number of elements currently in the queue
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        node = self._head.next
        length = 0
        while node:
            length += 1
            node = node.next
        return length

    def insert_front(self, value: object) -> None:
        """Add a new node with the given value at the beginning of the queue (right after the front sentinel).
        O(1) runtime complexity.
        """
        new_node = SLNode(value)
        if self.is_empty():
            self._tail = new_node
        new_node.next = self._head.next
        self._head.next = new_node

    def insert_back(self, value: object) -> None:
        """Add a new node with the given value at the end of the queue.
        O(N) runtime complexity.
        """
        new_node = SLNode(value)
        if self.is_empty():
            self._head.next = new_node
            self._tail = new_node
        else:
            self._tail.next = new_node
            self._tail = new_node

    def insert_at_index(self, index: int, value: object) -> None:
        """Insert a new value at the specified index position in the linked list.
        Index 0 refers to the beginning of the list (right after the front sentinel).
        If the provided index is invalid, raise a custom “QueueException”.
        Valid indices are [0, N] inclusive.
        O(N) runtime complexity.
        """
        if index < 0 or index > self.size():
            raise QueueException("Invalid index.")

        if index == 0:
            self.insert_front(value)
        elif index == self.size():
            self.insert_back(value)
        else:
            new_node = SLNode(value)
            prev_node = self._head
            for i in range(index):
                prev_node = prev_node.next
            new_node.next = prev_node.next
            prev_node.next = new_node

    def remove_at_index(self, index: int) -> None:
        """Remove the node at the specified index position from the linked list.
        Index 0 refers to the beginning of the list (right after the front sentinel).
        If the provided index is invalid, raise a custom “QueueException”.
        Valid indices are [0, N-1] inclusive.
        O(N) runtime complexity.
        """
        if index < 0 or index >= self.size():
            raise QueueException("Invalid index.")

        if index == 0:
            self._head.next = self._head.next.next
            if self._head.next is None:
                self._tail = None
        else:
            prev_node = self._head
            for i in range(index):
                prev_node = prev_node.next
            prev_node.next = prev_node.next.next
            if prev_node.next is None:
                self._tail = prev_node

    def remove(self, value: object) -> bool:
        """Remove the first node that matches the provided value.
        Return True if a node was removed, False otherwise.
        O(N) runtime complexity.
        """
        prev_node = self._head
        current_node = self._head.next

        while current_node:
            if current_node.value == value:
                prev_node.next = current_node.next
                if current_node.next is None:
                    self._tail = prev_node
                return True

            prev_node = current_node
            current_node = current_node.next

        return False

    def count(self, value: object) -> int:
        """Count the number of elements in the queue that match the provided value.
        O(N) runtime complexity.
        """
        count = 0
        node = self._head.next

        while node:
            if node.value == value:
                count += 1
            node = node.next

        return count

    def find(self, value: object) -> bool:
        """Check if the provided value exists in the queue.
        Return True if found, False otherwise.
        O(N) runtime complexity.
        """
        node = self._head.next

        while node:
            if node.value == value:
                return True
            node = node.next

        return False

    def slice(self, start_index: int, size: int) -> "Queue":
        """Return a new Queue that contains the requested number of nodes from the
        original queue, starting with the node located at the requested start index.
        If the provided start index is invalid or there are not enough nodes to make the slice,
        raise a custom “QueueException”.
        O(N) runtime complexity.
        """
        if start_index < 0 or start_index >= self.size() or size <= 0:
            raise QueueException("Invalid start index or size.")

        new_queue = Queue()
        count = 0
        node = self._head.next

        # Find the starting node for the slice
        while count < start_index:
            node = node.next
            count += 1

        # Slice the queue and create a new queue
        while count < start_index + size and node:
            new_queue.insert_back(node.value)
            node = node.next
            count += 1

        if count < start_index + size:
            raise QueueException("Not enough nodes to make the slice.")

        return new_queue

