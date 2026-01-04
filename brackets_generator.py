#!/usr/bin/env python3

from typing import Iterator
from operator import ge

class BracketGenerator:
    """Generates all valid bracket sequences using bit manipulation.
    
    Represents bracket sequences as binary numbers where 1 = '(' and 0 = ')'.
    Valid sequences have equal opening/closing brackets and maintain proper nesting.
    """
    
    def __init__(self, level: int):
        """Initialize generator for sequences with n pairs of brackets.
        
        Args:
            level: Number of bracket pairs to generate
        """
        self.level: int = level

    def brackets(self) -> Iterator[str]:
        """Generate all valid bracket sequences.
        
        Yields:
            Valid bracket strings with self.level pairs of brackets
        """
        return map(
            lambda num: self._convert_to_brackets(bin(num)[2:].zfill(self.level * 2)),
            filter(
                lambda num: all([
                        bin(num).count('1') == self.level,
                        self._is_valid_bracket_sequence(num),
                ]),
                self._rawrange()
            )
        )

    def _rawrange(self) -> range:
        """Return range of odd numbers representing potential bracket sequences.
        
        Step by 2 ensures rightmost bit is 1 (sequence starts with opening bracket).
        """
        return range(self._startvalue(), self._stopvalue(), 2)

    def _startvalue(self) -> int:
        """Calculate minimum binary value for valid sequences.
        
        Returns alternating 10 pattern: 101010... for self.level pairs.
        """
        return sum(map(lambda i: 2 ** (2 * i + 1), range(self.level)))

    def _stopvalue(self) -> int:
        """Calculate maximum binary value for the search range."""
        return 2 ** (2 * self.level) - 2 ** self.level + 2

    def _is_valid_bracket_sequence(self, value: int) -> bool:
        """Check if binary value represents valid bracket nesting.
        
        Validates that at each position, opening brackets >= closing brackets.
        
        Args:
            value: Binary number representing bracket sequence
            
        Returns:
            True if sequence maintains valid nesting throughout
        """
        return not any(
            map(
                lambda pos: ge(
                        (value % (2 ** (pos * 2 + 1))),
                        (2 ** (2 * pos + 1) - 2 ** pos)
                ),
                range(1, self.level)
            )
        )

    def _convert_to_brackets(self, binary_str: str) -> str:
        """Convert binary string to bracket string.
        
        Args:
            binary_str: Binary string where '1' = '(' and '0' = ')'
            
        Returns:
            Bracket sequence string
        """
        return ''.join(map(lambda bit: '(' if int(bit) else ')', binary_str))

if __name__ == "__main__":
    generator = BracketGenerator(15)
    for bracket_seq in generator.brackets():
        print(bracket_seq)
