#DynamicArray Class

from static_array import StaticArray


class DynamicArrayException(Exception):
    """Custom exception class to be used by Dynamic Array"""
    pass
class DynamicArray:
    def __init__(self, start_array=None):
        """Initialize new dynamic array"""
        self._size = 0
        self._capacity = 4
        self._data = StaticArray(self._capacity)
        # populate dynamic array with initial values (if provided)
        # before using this feature, implement append() method
        if start_array is not None:
            for value in start_array:
                self.append(value)
    def __str__(self) -> str:
        """Return content of dynamic array in human-readable form"""
        out = "DYN_ARR Size/Cap: "
        out += str(self._size) + "/" + str(self._capacity) + ' ['
        out += ', '.join([str(self._data[_]) for _ in range(self._size)])
        return out + ']'
    def __iter__(self):
        """Create iterator for loop"""
        self._index = 0
        return self
    def __next__(self):
        """Obtain next value and advance iterator"""
        try:
            value = self[self._index]
        except DynamicArrayException:
            raise StopIteration
        self._index += 1
        return value
    def get_at_index(self, index: int) -> object:
        """Return value from given index position
        Invalid index raises DynamicArrayException"""
        if index < 0 or index >= self._size:
            raise DynamicArrayException
        return self._data[index]
    def set_at_index(self, index: int, value: object) -> None:
        """Store value at given index in the array
        Invalid index raises DynamicArrayException"""
        if index < 0 or index >= self._size:
            raise DynamicArrayException
        self._data[index] = value
    def __getitem__(self, index) -> object:
        """Same functionality as get_at_index() method above,
        but called using array[index] syntax"""
        return self.get_at_index(index)
    def __setitem__(self, index, value) -> None:
        """Same functionality as set_at_index() method above,
        but called using array[index] syntax"""
        self.set_at_index(index, value)
    def is_empty(self) -> bool:
        """Return True is array is empty / False otherwise"""
        return self._size == 0
    def length(self) -> int:
        """Return number of elements stored in array"""
        return self._size
    def get_capacity(self) -> int:
        """Return the capacity of the array"""
        return self._capacity
    def print_da_variables(self) -> None:
        """Print information contained in the dynamic array.
        Used for testing purposes."""
        print(f"Length: {self._size}, Capacity: {self._capacity}, {self._data}")

    def resize(self, new_capacity: int) -> None:
        # Ensure that new_capacity is at least 4 (the default capacity)
        new_capacity = max(new_capacity, 4)

        if new_capacity >= self._size:
            new_data = StaticArray(new_capacity)
            for i in range(self._size):
                new_data[i] = self._data[i]

            self._data = new_data
            self._capacity = new_capacity

    def append(self, value: object) -> None:
        """Add a new value at the end of the dynamic array.
        If the internal storage associated with the dynamic array is already full,
        the capacity will be doubled using the `resize` method before adding the new value.
        """
        if self._size == self._data.length():
            self.resize(2 * self._data.length())

        self._data.set(self._size, value)
        self._size += 1

    def insert_at_index(self, index: int, value: object) -> None:
        """Add a new value at the specified index in the dynamic array.
        If the internal storage associated with the dynamic array is already full,
        the capacity will be doubled using the `resize` method before adding the new value.
        """
        if index < 0 or index > self._size:
            raise DynamicArrayException("Invalid index")

        if self._size == self._data.length():
            self.resize(2 * self._data.length())

        for i in range(self._size, index, -1):
            self._data.set(i, self._data.get(i - 1))

        self._data.set(index, value)
        self._size += 1

    def remove_at_index(self, index: int) -> None:
        """Remove the element at the specified index in the dynamic array."""
        if index < 0 or index >= self._size:
            raise DynamicArrayException("Invalid index")

        for i in range(index, self._size - 1):
            self._data.set(i, self._data.get(i + 1))

        self._data.set(self._size - 1, None)
        self._size -= 1

        # Reduce capacity if needed
        if self._size < self._data.length() // 4 and self._data.length() > 10:
            new_capacity = max(self._size * 2, 10)
            self.resize(new_capacity)

    def slice(self, start_index: int, size: int) -> object:
        """Return a new DynamicArray object that contains the requested elements from the original array.

    Args:
        start_index (int): The index of the first element to include in the slice.
        size (int): The number of elements to include in the slice.

    Raises:
        DynamicArrayException: If the provided start index or size is invalid,
            or if there are not enough elements to make the slice of the requested size.

    Returns:
        DynamicArray: A new DynamicArray object representing the slice.
        """
        if start_index < 0 or start_index >= self._size or size < 0 or start_index + size > self._size:
            raise DynamicArrayException("Invalid start index or size")

        new_da = DynamicArray()
        for element in range(start_index, start_index + size):
            new_da.append(self._data.get(element))

        return new_da

    def merge(self, second_da: object) -> None:
        """Append all elements from the input DynamicArray object onto the current one.

    Args:
        second_da (DynamicArray): The DynamicArray object whose elements will be appended.

    Note:
        The elements from the input DynamicArray are appended to the end of the current one,
        in the same order in which they are stored in the input array."""

        for element in range(second_da.length()):
            self.append(second_da._data.get(element))


    def map(self, map_func) -> object:
        """Create a new DynamicArray object where each element is derived by applying a given map_func to the original array.

    Args:
        map_func (function): The function to be applied to each element.

    Returns:
        DynamicArray: A new DynamicArray object containing the mapped values.
        """
        new_da = DynamicArray()
        for element in range(self._size):
            new_da.append(map_func(self._data.get(element)))
        return new_da

    def filter(self, filter_func) -> object:
        """Create a new DynamicArray object populated only with elements for which filter_func returns True.

    Args:
        filter_func (function): The filter function to be applied.

    Returns:
        DynamicArray: A new DynamicArray object containing the filtered elements.
        """
        new_da = DynamicArray()
        for element in range(self._size):
            if filter_func(self._data.get(element)):
                new_da.append(self._data.get(element))
        return new_da

    def reduce(self, reduce_func, initializer=None) -> object:
        """Sequentially applies the reduce_func to all elements of the dynamic array and returns the resulting value.

    Args:
        reduce_func (function): The reduce function to be applied.
        initializer (optional): The initial value for the reduction. Defaults to None.

    Returns:
        object: The result of the reduction.
        """
        if self._size == 0:
            return initializer

        if initializer is None:
            accumulator = self._data.get(0)
            start_index = 1
        else:
            accumulator = initializer
            start_index = 0

        for element in range(start_index, self._size):
            accumulator = reduce_func(accumulator, self._data.get(element))

        return accumulator