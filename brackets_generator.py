#!/usr/bin/env python3

from itertools import accumulate
from typing import Iterator

class BracketGenerator:
    def __init__(self, level: int):
        self.level: int = level

    def brackets(self) -> Iterator[str]:
        return map(
            lambda it: self._convert_list(bin(it)[2:].zfill(self.level * 2)),
            filter(
                lambda it: all([
                        bin(it).count('1') == self.level,
                        self._is_valid_bracket_sequence(it),
                ]),
                self._rawrange()
            )
        )

    def _fmtdrange(self) -> Iterator[str]:
        return map(lambda x: bin(x).lstrip('0b'), self._rawrange())

    def _rawrange(self) -> range:
        return range(self._startvalue(), self._stopvalue(), 2)

    def _startvalue(self) -> int:
        return sum(map(lambda it: 2 ** (2 * it + 1), range(self.level)))

    def _stopvalue(self) -> int:
        return 2 ** (2 * self.level) - 2 ** self.level + 2

    def _accum_ones(self, string: str) -> Iterator[int]:
        return accumulate(map(int, string[::-1]))

    def _block(self, string: str) -> Iterator[bool]:
        return map(lambda it: it[1] > it[0] - it[1] + 1, enumerate(self._accum_ones(string)))

    def _is_valid_bracket_sequence(self, value: int) -> bool:
        return not any(
            map(
                lambda it: (value % (2 ** (it * 2 + 1))) >= (2 ** (2 * it + 1) - 2 ** it),
                range(1, self.level)
            )
        )

    def _convert_list(self, lists: str) -> str:
        return ''.join(map(lambda it: '(' if int(it) else ')', lists))

if __name__ == "__main__":
    generator = BracketGenerator(15)
    for it in generator.brackets():
        print(it)
