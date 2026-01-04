#!/usr/bin/env python3
"""Benchmark comparison between bit manipulation and recursive bracket generation."""

import time
from typing import Iterator
from brackets_generator import BracketGenerator


class RecursiveBracketGenerator:
    """Classic recursive approach to generate valid bracket sequences."""
    
    def __init__(self, level: int):
        """Initialize generator for sequences with n pairs of brackets.
        
        Args:
            level: Number of bracket pairs to generate
        """
        self.level = level
    
    def brackets(self) -> Iterator[str]:
        """Generate all valid bracket sequences recursively.
        
        Yields:
            Valid bracket strings with self.level pairs of brackets
        """
        def generate(open_count: int, close_count: int, current: str):
            """Recursively build valid bracket sequences.
            
            Args:
                open_count: Number of opening brackets used so far
                close_count: Number of closing brackets used so far
                current: Current bracket string being built
            """
            if len(current) == self.level * 2:
                yield current
                return
            
            # Can add opening bracket if we haven't used all
            if open_count < self.level:
                yield from generate(open_count + 1, close_count, current + '(')
            
            # Can add closing bracket if it won't exceed opening brackets
            if close_count < open_count:
                yield from generate(open_count, close_count + 1, current + ')')
        
        yield from generate(0, 0, '')


def benchmark_generator(generator, name: str, level: int):
    """Benchmark a bracket generator.
    
    Args:
        generator: Generator instance to benchmark
        name: Name of the generator for display
        level: Level being tested
    """
    print(f"\n{name} (level {level}):")
    
    # Measure generation time
    start = time.perf_counter()
    count = sum(1 for _ in generator.brackets())
    elapsed = time.perf_counter() - start
    
    print(f"  Generated: {count:,} sequences")
    print(f"  Time: {elapsed:.3f} seconds")
    print(f"  Rate: {count/elapsed:,.0f} sequences/second")
    
    return elapsed, count


if __name__ == "__main__":
    LEVEL = 15
    print(f"Comparing bracket generation performance at level {LEVEL}")
    print("=" * 60)
    
    # Benchmark bit manipulation approach
    bit_gen = BracketGenerator(LEVEL)
    bit_time, bit_count = benchmark_generator(bit_gen, "Bit Manipulation", LEVEL)
    
    # Benchmark recursive approach
    rec_gen = RecursiveBracketGenerator(LEVEL)
    rec_time, rec_count = benchmark_generator(rec_gen, "Recursive", LEVEL)
    
    # Comparison
    print("\n" + "=" * 60)
    print("COMPARISON:")
    print(f"  Sequences generated: {bit_count:,} (both should match)")
    print(f"  Speedup: {rec_time/bit_time:.2f}x {'faster' if bit_time < rec_time else 'slower'}")
    if bit_time < rec_time:
        print(f"  Bit manipulation is {(rec_time-bit_time)/rec_time*100:.1f}% faster")
    else:
        print(f"  Recursive is {(bit_time-rec_time)/bit_time*100:.1f}% faster")
