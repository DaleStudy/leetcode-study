"""
주어진 문자열 s에서 최대 k번의 문자 교체를 통해
동일한 문자가 반복된 가장 긴 부분 문자열의 길이를 구해라

풀이: 슬라이딩 윈도우 + 빈도수 추적
"윈도우 [left, right] 구간에 대해,
해당 구간에서 최대 등장하는 문자 하나를 기준으로 나머지 문자들을 최대 k번까지 바꿔서 동일 문자로 만들 수 있나?"
-> 가능하면 윈도우 넓히기
-> 안되면 left를 줄여 윈도우 유지

현재 윈도우 길이: right - left + 1
윈도우 내 가장 자주 나온 문자 개수: max_cnt

if (right - left + 1) - max_cnt <= k:
    # 이 윈도우는 k번 교체로 모두 동일 문자 가능
    # -> 윈도우 확장
else:
    # 불가능 -> left를 오른쪽으로 줄여 윈도우 축소 (left + 1)

TC: O(N)
SC: O(1) -> dict는 최대 A-Z 26개의 키를 가짐 (상수 개수 제한)
"""

from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        english_char_dict = defaultdict(int)
        max_len = 0
        max_cnt = 0  # 현재 윈도우에서 가장 많이 나온 문자 수
        left = 0

        for right in range(len(s)):  # 0 ~ len(s)
            english_char_dict[s[right]] += 1  # 문자 등장 횟수 계산 
            max_cnt = max(max_cnt, english_char_dict[s[right]])  # 최대 등장 횟수 갱신

            # 현재 윈도우의 길이 = (right - left + 1)
            # 윈도우 내에서 바꿔야 할 문자 수가 k보다 크면 교체할 문자수가 너무 많으므로 윈도우 축소
            if (right - left + 1) - max_cnt > k:
                english_char_dict[s[left]] -= 1  # 왼쪽 문자 제거
                left += 1  # 윈도우 축소

            # 윈도우가 유효한 경우, 그 윈도우 길이로 최대 길이 갱신
            max_len = max(max_len, right - left + 1)

        return max_len
