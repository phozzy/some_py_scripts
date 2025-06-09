#!/usr/bin/env python3

"""Fibonacci sequence generator using a dataclass iterator."""

from dataclasses import dataclass
from itertools import islice

@dataclass
class FibonacciIterator:
    current_item: int = 0
    next_item: int = 1
    _index: int = 0

    def __iter__(self) -> 'FibonacciIterator':
        return self

    def __next__(self) -> int:
        buf: int = self.next_item
        self.next_item = buf + self.current_item
        self.current_item = buf
        self._index += 1
        return buf

def main():
    """Main function containing the script logic."""
    print("Fibonacci sequence:")
    fib = FibonacciIterator()
    
    for _ in range(10):
        print(next(fib))
    
    print("\nFirst 10 Fibonacci numbers (using for loop):")
    fib = FibonacciIterator()  # Reset iterator
    for num in islice(fib, 10):
        print(num)

if __name__ == "__main__":
    main()
