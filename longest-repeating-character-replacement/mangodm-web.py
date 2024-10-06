from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        - Idea: 슬라이딩 윈도우를 이용해 현재 윈도우 내에서 가장 자주 나타나는 문자의 개수를 추적한다.
          최대 k개의 문자를 바꿨을 때, 모든 문자가 같은 부분 문자열의 최대 길이를 계산한다.
          윈도우가 유효하지 않으면, 왼쪽 포인터를 이동시켜 윈도우 크기를 조정한다.
        - Time Complexity: O(n), n은 문자열의 길이다. 각 문자를 한번씩 순회하고, 슬라이딩 윈도우를 조정한다.
        - Space Complexity: O(26) = O(1), 슬라이딩 윈도우 내에 포함된 문자의 개수를 세기 위한 공간으로, 최대 알파벳 문자의 개수(26개)만큼 늘어날 수 있다.
        """
        result = 0
        counter = defaultdict(int)
        left = 0

        for right in range(len(s)):
            counter[s[right]] = counter[s[right]] + 1

            while (right - left + 1) - max(counter.values()) > k:
                counter[s[left]] -= 1
                left += 1

            result = max(result, right - left + 1)

        return result
