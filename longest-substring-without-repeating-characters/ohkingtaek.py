"""
Time Complexity: O(n^2)
Space Complexity: O(n)

과정:
1. 문자열을 순회하면서 중복되지 않는 가장 긴 부분 문자열을 찾음
2. 중복되지 않는 부분 문자열을 찾으면 그 길이를 최대 길이와 비교하여 최대 길이를 업데이트함
3. 중복되는 부분 문자열을 찾으면 그 부분 문자열을 초기화함
4. 중복되지 않는 부분 문자열을 찾으면 그 부분 문자열을 최대 길이와 비교하여 최대 길이를 업데이트함
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        for left in range(len(s)):
            tmp = set()
            for right in range(left, len(s)):
                if s[right] in tmp:
                    break
                tmp.add(s[right])
                ans = max(right - left + 1, ans)
        return ans
