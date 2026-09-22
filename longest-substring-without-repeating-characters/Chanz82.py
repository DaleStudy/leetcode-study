class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_len = 0
        visited = {}

        for right, ch in enumerate(s):
            if ch in visited and visited[ch] >= left: 
                left = visited[ch] + 1 # 현재 윈도우 상에서 중복 문자가 발견되었기 때문에 윈도우를 중복 문자 이후로 옮김.
            
            visited[ch] = right
            max_len = max(max_len, right - left + 1)

        return max_len
