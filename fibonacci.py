#!/usr/bin/env python3

"""Fibonacci sequence generator using a dataclass iterator."""

from dataclasses import dataclass

@dataclass
class FibonacciIterator:
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

def __main():
    """Main function containing the script logic."""
    print("Fibonacci sequence:")
    fib = FibonacciIterator()
    
    for _ in range(10):
        print(next(fib))

if __name__ == "__main__":
    __main()
