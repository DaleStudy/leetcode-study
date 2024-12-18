from typing import List

# Time Complexity O(n log n)
# - when sorting by sorted function(TimSort) for each string it takes O(nlogn)
# - traversing for loop takes O(n)
# Space Complexity O(n)
# - when sorting takes O(n)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_sorted = sorted(s)
        t_sorted = sorted(t)

        for i in range(len(s_sorted)):
            if s_sorted[i] != t_sorted[i]:
                return False
        return True

if __name__ == "__main__":
    solution = Solution()

    s = "nagaram"
    t = "anagram"

    result = solution.isAnagram(s, t)
    print(result)
