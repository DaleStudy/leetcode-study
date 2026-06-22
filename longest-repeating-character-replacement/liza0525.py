from collections import defaultdict


# 7기 풀이
# 시간 복잡도: O(n)
# - right는 매 루프마다 전진하고 left도 최대 n번 전진하므로 합쳐서 O(n)
# 공간 복잡도: O(1)
# - s에 있는 문자들의 개수만큼 공간 복잡도가 늘어나겠지만 모두 대문자인 알파벳만이 key로 들어오므로 최대 26개
class Solution:
    # 기본 아이디어: 슬라이딩 윈도우를 사용하면서
    # 윈도우 내에 가장 많이 있는 문자의 개수와 k값을 더한 값이 윈도우를 초과하는지 아닌지를 확인
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0  # 윈도우 왼쪽 인덱스 값
        max_len = 0  # 문제의 답(변경 시 가장 긴 substring 길이)
        char_dict = defaultdict(int)  # 윈도우 내의 각 문자들 개수를 확인하기 위한 dict
        max_char_cnt = 0  # 윈도우 내에 가장 많은 문자의 개수 그 자체(dict의 value() 메서드를 매번 호출하지 않게 하기 위함)

        for right in range(len(s)):  # 윈도우 오른쪽 인덱스 값
            char_dict[s[right]] += 1  # 오른쪽 인덱스에 해당하는 문자(예: A)에 대한 개수를 하나 올림
            max_char_cnt = max(max_char_cnt, char_dict[s[right]])  # 현재 윈도우에서 가장 많은 문자의 개수를 업데이트

            if max_char_cnt + k >= right - left + 1:
                # 가장 많은 문자열 사이에 있는 다른 문자들의 개수가 k보다 작으면 변경 가능
                # -> 윈도우 내에서 가장 긴 repeating substring을 만들 수 있음
                max_len = max(max_len, right - left + 1)
            else:
                # 만들 수 없는 경우에는 기존 left의 문자를 char_dict로부터 하나 줄이고
                # left를 하나 옮긴다(새로운 윈도우를 만든다는 의미)
                char_dict[s[left]] -= 1
                left += 1

        return max_len
