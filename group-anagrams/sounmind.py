from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Dictionary to store anagram groups using character frequency as key
        anagram_groups = defaultdict(list)

        for word in strs:
            # Create a frequency array for 26 lowercase English letters
            char_frequency = [0] * 26

            # Count frequency of each character in the current word
            for char in word:
                # Convert character to 0-25 index (a=0, b=1, ..., z=25)
                char_index = ord(char) - ord("a")
                char_frequency[char_index] += 1

            # Convert the frequency array to tuple (to make it hashable as dictionary key)
            # Words with identical character frequencies are anagrams
            freq_key = tuple(char_frequency)

            # Add the current word to its corresponding anagram group
            anagram_groups[freq_key].append(word)

        # Return all the anagram groups as a list of lists
        return list(anagram_groups.values())
