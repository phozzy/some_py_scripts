#!/usr/bin/env python3
"""Recursive bracket sequence generator - classic backtracking approach."""

from typing import Iterator


class BracketGenerator:
    """Generates all valid bracket sequences using recursion."""
    
    def __init__(self, level: int):
        """Initialize generator for sequences with n pairs of brackets.
        
        Args:
            level: Number of bracket pairs to generate
        """
        self.level: int = level
    
    def brackets(self) -> Iterator[str]:
        """Generate all valid bracket sequences recursively.
        
        Yields:
            Valid bracket strings with self.level pairs of brackets
        """
        def generate(open_count: int, close_count: int, current: str) -> Iterator[str]:
            """Recursively build valid bracket sequences.
            
            Args:
                open_count: Number of opening brackets used so far
                close_count: Number of closing brackets used so far
                current: Current bracket string being built
            """
            # Base case: we've used all brackets
            if open_count == self.level and close_count == self.level:
                yield current
                return
            
            # Can add opening bracket if we haven't used all
            if open_count < self.level:
                yield from generate(open_count + 1, close_count, current + '(')
            
            # Can add closing bracket if it won't exceed opening brackets
            if close_count < open_count:
                yield from generate(open_count, close_count + 1, current + ')')
        
        yield from generate(0, 0, '')


if __name__ == "__main__":
    generator = BracketGenerator(4)
    for bracket_seq in generator.brackets():
        print(bracket_seq)