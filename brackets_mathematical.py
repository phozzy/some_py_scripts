#!/usr/bin/env python3
"""Mathematical bracket sequence generator using Catalan number ranking/unranking.

This implementation uses combinatorial mathematics to directly compute the kth
bracket sequence without generating all previous sequences.
"""

from typing import Iterator
from functools import lru_cache


class MathematicalBracketGenerator:
    """Generate bracket sequences using mathematical ranking/unranking."""
    
    def __init__(self, level: int):
        """Initialize generator for sequences with n pairs of brackets.
        
        Args:
            level: Number of bracket pairs to generate
        """
        self.level = level
    
    @staticmethod
    @lru_cache(maxsize=None)
    def catalan(n: int) -> int:
        """Compute the nth Catalan number.
        
        C(n) = (2n)! / ((n+1)! * n!)
        
        Using the recurrence relation for efficiency:
        C(0) = 1
        C(n) = sum(C(i) * C(n-1-i)) for i = 0 to n-1
        
        Args:
            n: Index of Catalan number to compute
            
        Returns:
            The nth Catalan number
        """
        if n <= 1:
            return 1
        
        # Use dynamic programming to avoid overflow with large factorials
        result = 0
        for i in range(n):
            result += MathematicalBracketGenerator.catalan(i) * \
                     MathematicalBracketGenerator.catalan(n - 1 - i)
        return result
    
    def unrank(self, rank: int) -> str:
        """Convert a rank (index) to its corresponding bracket sequence.
        
        This uses the bijection between integers [0, C(n)-1] and valid
        bracket sequences of length 2n.
        
        Algorithm: Every valid sequence can be written as:
        '(' + left_part + ')' + right_part
        where left_part has i pairs, right_part has (n-1-i) pairs.
        
        The number of sequences with this structure is C(i) * C(n-1-i).
        
        Args:
            rank: Index of the sequence (0 to C(n)-1)
            
        Returns:
            The bracket sequence at the given rank
        """
        if self.level == 0:
            return ''
        
        # Find which "split" this rank falls into
        for i in range(self.level):
            # Number of sequences where left part has i pairs
            count = self.catalan(i) * self.catalan(self.level - 1 - i)
            
            if rank < count:
                # This rank falls in the current split
                left_rank = rank // self.catalan(self.level - 1 - i)
                right_rank = rank % self.catalan(self.level - 1 - i)
                
                # Recursively unrank left and right parts
                left_gen = MathematicalBracketGenerator(i)
                right_gen = MathematicalBracketGenerator(self.level - 1 - i)
                
                left_part = left_gen.unrank(left_rank)
                right_part = right_gen.unrank(right_rank)
                
                return '(' + left_part + ')' + right_part
            
            rank -= count
        
        # Should never reach here for valid rank
        raise ValueError(f"Invalid rank: {rank}")
    
    def rank(self, sequence: str) -> int:
        """Convert a bracket sequence to its rank (index).
        
        This is the inverse of unrank().
        
        Args:
            sequence: A valid bracket sequence
            
        Returns:
            The rank of the sequence (0 to C(n)-1)
        """
        if len(sequence) == 0:
            return 0
        
        rank = 0
        depth = 0
        
        # Find where the first '(' closes
        for idx, bracket in enumerate(sequence):
            if bracket == '(':
                depth += 1
            else:
                depth -= 1
                
            if depth == 0:
                # Found the matching ')' for the first '('
                # The sequence is: '(' + left + ')' + right
                i = idx // 2  # Number of pairs in left part
                
                left_part = sequence[1:idx]
                right_part = sequence[idx+1:]
                
                # Add ranks for all splits before this one
                for j in range(i):
                    rank += self.catalan(j) * self.catalan(self.level - 1 - j)
                
                # Add rank within this split
                if i > 0:
                    left_gen = MathematicalBracketGenerator(i)
                    left_rank = left_gen.rank(left_part)
                    rank += left_rank * self.catalan(self.level - 1 - i)
                
                if self.level - 1 - i > 0:
                    right_gen = MathematicalBracketGenerator(self.level - 1 - i)
                    rank += right_gen.rank(right_part)
                
                break
        
        return rank
    
    def brackets(self) -> Iterator[str]:
        """Generate all valid bracket sequences in lexicographic order.
        
        Yields:
            Valid bracket strings with self.level pairs of brackets
        """
        total = self.catalan(self.level)
        for rank in range(total):
            yield self.unrank(rank)


if __name__ == "__main__":
    # Demo with level 4
    level = 4
    generator = MathematicalBracketGenerator(level)
    
    print(f"Generating all bracket sequences for level {level}")
    print(f"Total sequences (Catalan number): {generator.catalan(level)}")
    print("\nRank -> Sequence:")
    print("-" * 40)
    
    for rank, seq in enumerate(generator.brackets()):
        print(f"{rank:2d}: {seq}")
    
    # Demo random access
    print("\n" + "=" * 40)
    print("Random access examples:")
    print("-" * 40)
    
    test_ranks = [0, 5, 13]
    for rank in test_ranks:
        seq = generator.unrank(rank)
        computed_rank = generator.rank(seq)
        print(f"Rank {rank}: {seq} (verify: rank={computed_rank})")
    
    # Demo with larger level
    print("\n" + "=" * 40)
    level = 10
    generator_large = MathematicalBracketGenerator(level)
    print(f"Level {level}: {generator_large.catalan(level):,} sequences")
    print(f"First sequence: {generator_large.unrank(0)}")
    print(f"Middle sequence: {generator_large.unrank(generator_large.catalan(level) // 2)}")
    print(f"Last sequence: {generator_large.unrank(generator_large.catalan(level) - 1)}")
