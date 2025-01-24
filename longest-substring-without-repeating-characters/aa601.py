# TC:O(n^2) SC:O(1)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_size = 0
        for start in range(len(s)):
            saw = set()
            for end in range(start, len(s)):
                if s[end] in saw:
                    break
                else:
                    saw.add(s[end])
                    max_size = max(max_size, end - start + 1) # 부분 문자열의 길이와 현재까지의 최대길이값 비교
        return max_size
