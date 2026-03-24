#!/usr/bin/env python3

"""Fibonacci sequence generator using a dataclass iterator."""

from dataclasses import dataclass, field
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

    Example:
        >>> fib = FibonacciIterator()
        >>> for i, num in enumerate(fib):
        ...     print(num)
        ...     if i >= 5:
        ...         break
        0
        1
        1
        2
        3
        5

    Methods:
        __iter__(): Returns the iterator object itself.
        __next__(): Returns the next Fibonacci number in the sequence.
        reset(): Resets the iterator back to the beginning of the sequence.
    """
    current_item: int = field(default=0, init=False)
    next_item: int = field(default=1, init=False)

    def __iter__(self) -> 'FibonacciIterator':
        return self

    def __next__(self) -> int:
        result: int = self.current_item
        (
            self.current_item,
            self.next_item,
        ) = (
            self.next_item,
            self.current_item + self.next_item,
        )
        return result
    
    def reset(self) -> None:
        """Reset the iterator back to the beginning of the Fibonacci sequence."""
        self.current_item = 0
        self.next_item = 1

def get_nth(n: int) -> int:
    """
    Get the nth Fibonacci number.

    Args:
        n (int): The index of the Fibonacci number to retrieve (0-indexed).

    Returns:
        int: The nth Fibonacci number.

    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError(f"n must be non-negative, got {n}")
    
    fib: FibonacciIterator = FibonacciIterator()
    return next(
        islice(
            fib,
            n,
            n + 1,
        )
    )

def fibonacci(n: int) -> list[int]:
    """
    Get the first n Fibonacci numbers.

    Args:
        n (int): Number of Fibonacci numbers to return.

    Returns:
        list[int]: List containing the first n Fibonacci numbers.

    Raises:
        ValueError: If n is negative.
    
    Example:
        >>> fibonacci(5)
        [0, 1, 1, 2, 3]
        >>> fibonacci(10)
        [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    """
    if n < 0:
        raise ValueError(f"n must be non-negative, got {n}")
    
    if n == 0:
        return []
    
    fib: FibonacciIterator = FibonacciIterator()
    return list(islice(fib, n))

def main():
    """Main function containing the script logic."""
    print("Fibonacci sequence:")
    fib: FibonacciIterator = FibonacciIterator()

    for _ in range(10):
        print(next(fib))

    print("\n10th Fibonacci number:")
    print(get_nth(10))
    
    print("\nFirst 10 Fibonacci numbers:")
    print(fibonacci(10))
    
    print("\nReset demo:")
    fib.reset()
    print(f"After reset: {[next(fib) for _ in range(5)]}")

if __name__ == "__main__":
    main()
