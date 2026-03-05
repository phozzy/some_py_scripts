def print_formatted(number: int) -> None:
    width: int = len(bin(number).lstrip('0b'))  # Get the width based on the binary representation of the number
    for i in range(1, number + 1):
        decimal_str: str = str(i).rjust(width, ' ')
        octal_str: str = oct(i).lstrip('0o').rjust(width, ' ')
        hex_str: str = hex(i).lstrip('0x').upper().rjust(width, ' ')
        binary_str: str = bin(i).lstrip('0b').rjust(width, ' ')
        print(f"{decimal_str} {octal_str} {hex_str} {binary_str}")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)