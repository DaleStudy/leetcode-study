from collections import Counter

# first solution -> O(N**2), time limit exceeded
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 0

        # window : length of the substring
        for window in range(1, len(s)+1):
            for i in range(len(s) - window + 1):
                substring = s[i:i+window]

                counter = Counter(substring)
                max_count = max(counter.values())
                if window - max_count <= k:
                    max_length = max(max_length, window)

        return max_length

# second solution
from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 0
        counter = Counter()
        left = 0

        for right in range(len(s)):
            counter[s[right]] += 1
            max_count = max(counter.values())

            window = right - left + 1
            # window 사이즈가 조건에 맞도록 줄이기
            while window - max_count > k:
                counter[s[left]] -= 1
                left += 1
                max_count = max(counter.values())
                window = right - left + 1 # update the window size because left has been moved

            # 조건을 만족하는 window size 로 max length 를 갱신한다.
            max_length = max(window, max_length)

        return max_length
