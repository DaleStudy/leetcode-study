"""
 * Time Complexity: O(n)
 * Space Complexity: O(1) => 길이 26으로 고정된 배열이므로 O(1)
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = [0] * 26
        for c1, c2 in zip(s, t):
            count[ord(c1) - ord('a')] += 1
            count[ord(c2) - ord('a')] -= 1

        return all(c == 0 for c in count)
