# Time: O(n log n), Space: O(n)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return (
            False if len(s) != len(t)
            else False if sorted(s) != sorted(t)
            else True
        )

