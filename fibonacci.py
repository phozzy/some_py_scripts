#!/usr/bin/env python3

"""Fibonacci sequence generator using a dataclass iterator."""

from dataclasses import dataclass
from itertools import islice

@dataclass
class FibonacciIterator:
    """
    An iterator that generates Fibonacci sequence numbers.

    This iterator produces an infinite sequence of Fibonacci numbers starting from 0, 1.
    Each call to __next__() returns the next number in the sequence.

    Attributes:
        current_item (int): The current Fibonacci number in the sequence.
        next_item (int): The next Fibonacci number to be returned.
        _index (int): Internal counter tracking the position in the sequence.

    Example:
        >>> fib = FibonacciIterator()
        >>> for i, num in enumerate(fib):
        ...     print(num)
        ...     if i >= 5:
        ...         break
        1
        1
        2
        3
        5
        8

    Methods:
        __iter__(): Returns the iterator object itself.
        __next__(): Returns the next Fibonacci number in the sequence.
    """
    current_item: int = 0
    next_item: int = 1
    _index: int = 0

    def __iter__(self) -> 'FibonacciIterator':
        return self

    def __next__(self) -> int:
        (
            self.current_item,
            self.next_item,
        ) = (
            self.next_item,
            self.current_item + self.next_item,
        )
        self._index += 1
        return self.current_item

def get_nth(n: int) -> int:
    """
    Get the nth Fibonacci number.

    Args:
        n (int): The index of the Fibonacci number to retrieve (0-indexed).

    Returns:
        int: The nth Fibonacci number.

    Raises:
        StopIteration: If the iterator is exhausted before reaching the nth element.
    """
    fib: FibonacciIterator = FibonacciIterator()
    return next(
        islice(
            fib,
            n,
            n + 1,
        )
    )

def __main():
    """Main function containing the script logic."""
    print("Fibonacci sequence:")
    fib = FibonacciIterator()

    for _ in range(10):
        print(next(fib))

    print("\n10th Fibonacci number:")
    print(get_nth(10))

if __name__ == "__main__":
    __main()
