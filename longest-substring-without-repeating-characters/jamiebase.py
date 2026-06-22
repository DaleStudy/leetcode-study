"""
# Approach
슬라이딩 윈도우를 사용한다.
right 포인터를 하나씩 이동시키면서 문자열을 확장하고,
이미 등장한 문자를 만나면 해당 문자의 마지막 위치를 기준으로 left 포인터를 이동시켜 중복이 없는 구간을 유지한다.
각 단계에서 현재 윈도우의 길이를 계산하여 최대값을 갱신한다.

# Complexity
문자열 길이를 N이라고 할 때, 문자 종류 수를 K라고 할 때
- Time complexity: O(N)
- Space complexity: O(K)
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}  # 문자 -> 마지막으로 등장한 인덱스
        left = 0  # 현재 윈도우의 시작 위치
        answer = 0  # 최대 길이 저장

        for right, ch in enumerate(s):
            # 현재 문자가 이전에 등장했고,
            # 그 위치가 현재 윈도우 안에 있다면 left 이동
            if ch in last_seen and last_seen[ch] >= left:
                left = last_seen[ch] + 1

            # 현재 문자의 마지막 위치 갱신
            last_seen[ch] = right

            # 현재 윈도우 길이 계산 및 최대값 갱신
            answer = max(answer, right - left + 1)

        return answer
