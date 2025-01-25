"""
Solution: 
    1) for iteration 을 도는 동안 hash set 을 이용해 처음 발견한 원소들을 window set에 넣는다.
    2) 중복되는 원소를 발견할 경우 해당 원소의 중복이 사라질때까지 left side 의 원소들을 하나씩 제거한다.

Time: O(n^2) = O(n) (for iteration) * O(n) 최악의 경우 n만큼의 중복제거 
Space: O(n) (모든 원소가 set에 들어갈 경우)
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        max_len = 0
        l = 0
        for r in range(len(s)):
            while s[r] in window:
                window.remove(s[l])
                l += 1
            window.add(s[r])
            max_len = max(max_len, len(window))
        return max_len
