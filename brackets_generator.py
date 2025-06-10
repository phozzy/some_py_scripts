#!/usr/bin/env python3

from typing import Iterator
from operator import ge

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

    def _rawrange(self) -> range:
        return range(self._startvalue(), self._stopvalue(), 2)

    def _startvalue(self) -> int:
        return sum(map(lambda it: 2 ** (2 * it + 1), range(self.level)))

    def _stopvalue(self) -> int:
        return 2 ** (2 * self.level) - 2 ** self.level + 2

    def _is_valid_bracket_sequence(self, value: int) -> bool:
        return not any(
            map(
                lambda it: ge(
                        (value % (2 ** (it * 2 + 1))),
                        (2 ** (2 * it + 1) - 2 ** it)
                ),
                range(1, self.level)
            )
        )

    def _convert_list(self, lists: str) -> str:
        return ''.join(map(lambda it: '(' if int(it) else ')', lists))

if __name__ == "__main__":
    generator = BracketGenerator(15)
    for it in generator.brackets():
        print(it)
