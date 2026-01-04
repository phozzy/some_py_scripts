#!/usr/bin/env python3
"""Test memory usage of different bracket generation approaches."""

import tracemalloc
import sys
from brackets_generator import BracketGenerator
from benchmark_brackets import RecursiveBracketGenerator


def measure_memory(generator, name: str, level: int, collect_all: bool = False):
    """Measure memory usage of a bracket generator.
    
    Args:
        generator: Generator instance to test
        name: Name for display
        level: Level to test
        collect_all: If True, collect all results in a list (high memory)
                     If False, iterate without storing (low memory)
    """
    print(f"\n{name} (level {level}, {'collecting all' if collect_all else 'iterating'})")
    
    tracemalloc.start()
    
    if collect_all:
        # Store all results in memory (bad for large levels!)
        results = list(generator.brackets())
        count = len(results)
    else:
        # Iterate without storing (memory efficient)
        count = sum(1 for _ in generator.brackets())
    
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    print(f"  Sequences: {count:,}")
    print(f"  Current memory: {current / 1024 / 1024:.2f} MB")
    print(f"  Peak memory: {peak / 1024 / 1024:.2f} MB")
    
    return peak


if __name__ == "__main__":
    print("Memory Usage Comparison")
    print("=" * 60)
    
    # Test at smaller level first
    LEVEL = 12
    print(f"\nTesting at level {LEVEL} (114,334 sequences)")
    
    # Bit manipulation - iterate only
    bit_gen = BracketGenerator(LEVEL)
    bit_mem = measure_memory(bit_gen, "Bit Manipulation", LEVEL, collect_all=False)
    
    # Recursive - iterate only
    rec_gen = RecursiveBracketGenerator(LEVEL)
    rec_mem = measure_memory(rec_gen, "Recursive", LEVEL, collect_all=False)
    
    print("\n" + "=" * 60)
    print("ITERATING (memory efficient):")
    print(f"  Bit manipulation peak: {bit_mem / 1024 / 1024:.2f} MB")
    print(f"  Recursive peak: {rec_mem / 1024 / 1024:.2f} MB")
    
    # Now test with collecting all results (memory intensive)
    print("\n" + "=" * 60)
    print(f"\nCollecting ALL results in memory (at level {LEVEL}):")
    
    bit_gen2 = BracketGenerator(LEVEL)
    bit_mem2 = measure_memory(bit_gen2, "Bit Manipulation", LEVEL, collect_all=True)
    
    rec_gen2 = RecursiveBracketGenerator(LEVEL)
    rec_mem2 = measure_memory(rec_gen2, "Recursive", LEVEL, collect_all=True)
    
    print("\n" + "=" * 60)
    print("COLLECTING ALL (memory intensive):")
    print(f"  Bit manipulation peak: {bit_mem2 / 1024 / 1024:.2f} MB")
    print(f"  Recursive peak: {rec_mem2 / 1024 / 1024:.2f} MB")
    
    print("\n" + "=" * 60)
    print("KEY INSIGHT:")
    print("  Both approaches use generators (lazy evaluation)")
    print("  When iterating: minimal memory (only current sequence)")
    print("  When collecting: memory proportional to output size")
    print("  Recursive uses call stack memory: ~O(2*level) depth")
