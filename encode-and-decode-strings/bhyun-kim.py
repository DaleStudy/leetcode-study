"""
271. Encode and Decode Strings
https://leetcode.com/problems/encode-and-decode-strings/description/

Solution:
    - Concatenate the strings with a special character
    - Split the string by the special character

Time complexity: O(n)
    - Concatenating the strings: O(n)
    - Splitting the string: O(n)
    - Total: O(n)

Space complexity: O(n)
    - Storing the output: O(n)
    - Total: O(n)
"""
from typing import List


class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string."""
        output = strs[0]

        for i in range(1, len(strs)):
            output += "é" + strs[i]

        return output

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings."""

        return s.split("é")
