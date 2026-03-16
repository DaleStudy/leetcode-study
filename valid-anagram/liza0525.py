from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 1. s를 구성하고 있는 각 알파벳과 그 알파벳이 존재하는 개수를 세기 위해
        # defaultdict로 dictionary 만들어준다.
        alphabet_cnt_dict = defaultdict(int)

        # 2. s의 알파벳을 탐색하면서 alphabet_cnt_dict에서 count(value)를 하나씩 증가
        # 예시: anagram의 경우, {"a": 3, "n": 1, "g": 1, "m": 1, "r": 1}이 최종 값이 됨
        for ss in s:
            alphabet_cnt_dict[ss] += 1
        
        # 3. t의 알파벳을 탐색하면서 alphabet_cnt_dict에서 count(value)를 하나씩 감소
        # 예시: anagram의 아나그램인 경우, {"a": 0, "n": 0, "g": 0, "m": 0, "r": 0}이 최종 값이 됨
        for tt in t:
            alphabet_cnt_dict[tt] -= 1

        # 4. s와 t가 서로 아나그램이었다면, 구성했던 모든 알파벳에 대해 count 값이 0으로 변경되어 있어야 함
        # 그렇지 않으면(양수 또는 음수 값이 존재하면) 아나그램이라고 할 수 없다.
        for cnt in alphabet_cnt_dict.values():
            if cnt != 0:
                return False
        return True



# 7기 풀이
# 시간 복잡도: O(n)
#  - s, t, letter_dict를 모두 한 loop당 한 번 씩만 돈다.
# 공간 복잡도: O(n)
#  - letter_dict 생성 시 s의 길이(n이라고 할 때)에 종속된다.
from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s를 구성하는 각 알파벳의 개수를 저장할 defaultdict을 생성 
        letter_dict = defaultdict(int)

        # s의 문자열을 돌며 각 알파벳의 개수를 카운트
        for ss in s:
            letter_dict[ss] += 1

        # t 문자열을 돌만셔 각 알파벳의 개수만큼 dictionary에서 빼준다.
        for tt in t:
            letter_dict[tt] -= 1

        # s, t를 돌며 각 알파벳의 개수를 센 후 value들은 모두 0이 되어야 한다. (아나그램 특성 상)
        # 각 알파벳의 value가 양수면 s에 더 많았고, 음수면 t가 더 많았다는 의미가 됨
        for v in letter_dict.values():
            if v != 0:
                return False

        return True
