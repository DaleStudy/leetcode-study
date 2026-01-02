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
