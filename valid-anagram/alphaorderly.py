class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
            O(N Log N)
        """
        return sorted(s) == sorted(t)

# class Solution:
#     """
#         O(N)
#     """
#     def isAnagram(self, s: str, t: str) -> bool:
#         return Counter(s) == Counter(t)
