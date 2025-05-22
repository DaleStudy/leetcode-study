# https://leetcode.com/problems/longest-repeating-character-replacement/

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        [Complexity]
            - TC: O(n)
            - SC: O(n)

        [Approach]
            two pointer로 sliding window를 이동해가면서, k번 이내로 replace 했을 때 모두 같은 문자가 될 때의 max_len를 트래킹하면 된다.
            이때, 이 substring을 모두 같은 문자로 만들 수 있는 가장 작은 replacement 횟수를 구해 k와 비교해야 하는데,
            이 횟수 max_replace는 (substring의 길이 - 가장 빈도가 높은 문자의 등장 횟수) 이다.
            max_replace가 k 이하라면 max_len을 업데이트하고, 아니라면 left를 한 칸 전진한다.
        """
        from collections import defaultdict

        left = max_len = max_freq = 0  # left ~ right: k번 이내로 replace 했을 때, 모두 같은 문자일 때의 max_len 업데이트
        cnt = defaultdict(int)  # left ~ right sliding window 내에서의 counter

        # right 한 칸씩 이동해가며 확인
        for right in range(len(s)):
            # max_freq 업데이트
            cnt[s[right]] += 1
            max_freq = max(max_freq, cnt[s[right]])

            # 현재 sliding window를 모두 같은 문자로 만들 수 있는 가장 작은 replacement 횟수 구하기
            sub_len = right - left + 1
            min_replace = sub_len - max_freq

            # min_replace가 k 이하이면, max_len 업데이트
            if min_replace <= k:
                max_len = max(max_len, sub_len)
            # 아니라면, left 한 칸 이동
            else:
                cnt[s[left]] -= 1
                left += 1

        return max_len
