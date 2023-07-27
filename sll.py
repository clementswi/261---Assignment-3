# Name: William Clements
# OSU Email: clementsw@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 3, Part 5
# Due Date: 7/24/2023 (Note: 2 free days used on this assignment)
# Description: Queue class

from SLNode import *


class SLNode:
    """Singly Linked List Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY"""

    def __init__(self, value: object, next=None) -> None:
        self.value = value
        self.next = next


class SLLException(Exception):
    """Custom exception to be used by LinkedList class
    DO NOT CHANGE THIS CLASS IN ANY WAY"""
    pass


class LinkedList:
    def __init__(self):
        """Initialize a new LinkedList with a front sentinel node
        DO NOT CHANGE THIS METHOD IN ANY WAY"""
        self._head = SLNode(None)

    def __str__(self):
        """Return content of the linked list in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY"""
        out = 'SLL ['
        if not self.is_empty():
            node = self._head.next
            out += str(node.value)
            node = node.next
            while node:
                out += ' -> ' + str(node.value)
                node = node.next
        return out + ']'

    def is_empty(self) -> bool:
        """Return True if the linked list is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._head.next is None

    def insert_front(self, value: object) -> None:
        """Insert a new node with the given value at the beginning of the list (after the front sentinel).
        O(1) runtime complexity.
        """
        new_node = SLNode(value)
        new_node.next = self._head.next
        self._head.next = new_node

    def insert_back(self, value: object) -> None:
        """Insert a new node with the given value at the end of the list.
        O(N) runtime complexity.
        """
        new_node = SLNode(value)
        node = self._head
        while node.next:
            node = node.next
        node.next = new_node

    def insert_at_index(self, index: int, value: object) -> None:
        """Insert a new value at the specified index position in the linked list.
        Index 0 refers to the beginning of the list (right after the front sentinel).
        If the provided index is invalid, raise a custom "SLLException".
        O(N) runtime complexity.
        """
        if index < 0:
            raise SLLException("Invalid index: Index must be non-negative.")

        new_node = SLNode(value)
        prev_node = self._head
        node = self._head.next
        current_index = 0

        while node and current_index < index:
            prev_node = node
            node = node.next
            current_index += 1

        if current_index == index:
            prev_node.next = new_node
            new_node.next = node
        else:
            raise SLLException("Invalid index: Index out of range.")

    def remove_at_index(self, index: int) -> None:
        """Remove the node at the specified index position from the linked list.
        Index 0 refers to the beginning of the list (right after the front sentinel).
        If the provided index is invalid, raise a custom "SLLException".
        O(N) runtime complexity.
        """
        if index < 0:
            raise SLLException("Invalid index: Index must be non-negative.")

        prev_node = self._head
        node = self._head.next
        current_index = 0

        while node and current_index < index:
            prev_node = node
            node = node.next
            current_index += 1

        if current_index == index:
            if node:
                prev_node.next = node.next
            else:
                raise SLLException("Invalid index: Index out of range.")
        else:
            raise SLLException("Invalid index: Index out of range.")

    def remove(self, value: object) -> bool:
        """Remove the first occurrence of the node with the given value from the linked list.
        Return True if a node was removed from the list, otherwise return False.
        O(N) runtime complexity.
        """
        prev_node = self._head
        node = self._head.next

        while node:
            if node.value == value:
                prev_node.next = node.next
                return True
            prev_node = node
            node = node.next

        return False

    def count(self, value: object) -> int:
        """Count the number of elements in the list that match the provided value.
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
        """Check if the provided value exists in the list.
        Return True if the value is found, otherwise return False.
        O(N) runtime complexity.
        """
        node = self._head.next

        while node:
            if node.value == value:
                return True
            node = node.next

        return False

    def slice(self, start_index: int, size: int) -> 'LinkedList':
        """Return a new LinkedList containing the requested number of nodes from the original list,
        starting with the node located at the requested start index.
        If the provided start index is invalid, or if there are not enough nodes between the start index
        and the end of the list to make a slice of the requested size, raise a custom "SLLException".
        O(N) runtime complexity.
        """
        if start_index < 0:
            raise SLLException("Invalid start index: Index must be non-negative.")

        new_list = LinkedList()
        node = self._head.next
        current_index = 0

        # Move to the start index
        while node and current_index < start_index:
            node = node.next
            current_index += 1

        if current_index != start_index:
            raise SLLException("Invalid start index: Index out of range.")

        # Add nodes to the new list up to the requested size
        while node and size > 0:
            new_list.insert_back(node.value)
            node = node.next
            size -= 1

        if size > 0:
            raise SLLException("Not enough nodes to make a slice of the requested size.")

        return new_list

