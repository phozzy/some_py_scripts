#!/usr/bin/env python3

from enum import Enum


class AllowedChar(Enum):
    """Enum containing only allowed characters."""
    PIPE = '|'
    DOT = '.'
    DASH = '-'
    W = 'W'
    E = 'E'
    L = 'L'
    C = 'C'
    O = 'O'
    M = 'M'

class AllowedString:
    """A string that can only contain characters from AllowedChar enum."""
    
    _allowed_chars = {char.value for char in AllowedChar}
    
    def __init__(self, value: str):
        for c in value:
            if c not in self._allowed_chars:
                raise ValueError(f"Invalid character: '{c}'")
        self._value = value
    
    def __str__(self) -> str:
        return self._value
    
    def __repr__(self) -> str:
        return f"AllowedString({self._value!r})"
    
    def __len__(self) -> int:
        return len(self._value)
    
    def __getitem__(self, index: int | slice) -> str:
        return self._value[index]
    
    def __eq__(self, other: object) -> bool:
        if isinstance(other, AllowedString):
            return self._value == other._value
        return False
    
    @property
    def value(self) -> str:
        return self._value


# Type alias for a list of allowed strings
AllowedStringList = list[AllowedString]


def create_allowed_string(size: int, row: int) -> AllowedString:
    """
    Creates an AllowedString from two numbers.
    
    Args:
        size: Size of the string
        row: Row number
    
    Returns:
        An AllowedString composed of allowed characters
    """
    dashes: AllowedString = AllowedString('---')
    sign: AllowedString = AllowedString('.|.')
    number_of_signs: int = row * 2 + 1
    number_of_dashes: int = size // 2 - row
    # result = str(dashes * number_of_dashes + sign * number_of_signs + dashes * number_of_dashes)
    result: AllowedString = AllowedString(
        dashes.value * number_of_dashes + sign.value * number_of_signs + dashes.value * number_of_dashes
    )
    return result

def create_door_mat(size: int):
    for row in range(size // 2):
        yield create_allowed_string(size, row)
    yield create_welcome_string(size)
    for row in range(size // 2 - 1, -1, -1):
        yield create_allowed_string(size, row)

def create_welcome_string(size: int) -> AllowedString:
    number_of_dashes: int = ((3 * size) - 7) // 2
    dashes: AllowedString = AllowedString('-')
    welcome: AllowedString = AllowedString('WELCOME')
    result: AllowedString = AllowedString(
        dashes.value * number_of_dashes + welcome.value + dashes.value * number_of_dashes
    )
    return result

def check_numbers() -> tuple[int, int]:
    """
    Read and validate two numbers from stdin.
    First number: odd and within range (5, 100)
    Second number: must be 3 times the first number and within range (15, 303)
    Raises ValueError if validation fails.
    Returns tuple of (first, second) if valid.
    """
    user_input: str = input().strip()
    
    # Try to parse two numbers
    parts = user_input.split()
    if len(parts) != 2:
        raise ValueError("Please enter exactly two numbers separated by space.")
    
    try:
        first: int = int(parts[0])
        second: int = int(parts[1])
    except ValueError as e:
        raise ValueError(f"Invalid input: {e}")
    
    # Validate first number is odd
    if first % 2 == 0:
        raise ValueError(f"First number {first} must be odd")
    
    # Validate first number is in range (greater than 5 and less than 100)
    if not (5 < first < 101):
        raise ValueError(f"First number {first} must be greater than 5 and less than 101")
    
    # Validate second number is 3 times the first
    if second != 3 * first:
        raise ValueError(f"Second number {second} must be 3 times the first ({3 * first})")
    
    # Validate second number is in range (greater than 15 and less than 303)
    if not (15 < second < 303):
        raise ValueError(f"Second number {second} must be greater than 15 and less than 303")
    
    return (first, second)


def main() -> None:
    """Main entry point for the program."""
    first, second = check_numbers()
    for line in create_door_mat(first):
        print(line)

if __name__ == "__main__":
    main()
