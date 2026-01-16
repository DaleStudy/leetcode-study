class Solution:
    def countSubstrings(self, s: str) -> int:
        total_count = 0

        def expand(left, right):
            local_count = 0
            while left>=0 and right< len(s) and s[left] == s[right]:
            # while s[left] == s[right] and left>=0 and right< len(s) :
            # The above line would cause index error if left or right go out of bounds
                local_count += 1
                left -= 1
                right += 1
            return local_count

        for i in range(len(s)):
            total_count += expand(i, i)
            total_count += expand(i, i+1)
        
        return total_count
    
#Complexity Analysis
#Time complexity: O(n^2) where n is the length of the input string s.
#Space complexity: O(1) as we are using only a constant amount of extra space
# Manacher's Algorithm can achieve O(n) time complexity for this problem.

