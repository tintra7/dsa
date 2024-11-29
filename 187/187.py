from typing import List

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []

        base = 4  # We use 4 as the base since there are 4 possible nucleotides: A, C, G, T
        mod = 2**20  # A large modulus (2^20) to prevent overflow

        # Map nucleotides to integers
        char_to_int = {'A': 0, 'C': 1, 'G': 2, 'T': 3}

        hash_value = 0
        seen_hashes = set()
        repeated_sequences = set()

        # Rolling hash for the first 10 characters
        for i in range(10):
            hash_value = (hash_value * base + char_to_int[s[i]]) % mod
        seen_hashes.add(hash_value)

        # Slide the window
        for i in range(10, len(s)):
            # Remove the leftmost character and add the new character
            hash_value = (hash_value * base + char_to_int[s[i]] -
                        char_to_int[s[i - 10]] * (base**10)) % mod
            # Ensure hash is positive
            if hash_value < 0:
                hash_value += mod

            # Check for repeats
            if hash_value in seen_hashes:
                repeated_sequences.add(s[i - 9:i + 1])
            else:
                seen_hashes.add(hash_value)

        return list(repeated_sequences)

s = Solution()
print(s.findRepeatedDnaSequences(s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))