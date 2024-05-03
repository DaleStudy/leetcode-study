# 문제: https://leetcode.com/problems/valid-anagram/
from collections import defaultdict


# 풀이: s 와 t 에 입력된 알파벳의 갯수를 체크한다. ...
# 애너그램이면 T
def is_anagram(s, t) -> bool:
    # 글자수가 같다는 조건이 없음.
    if len(s) != len(t):
        return False

    word_counter = defaultdict(int)
    # s 문자열 분해
    for alpha in s:
        word_counter[alpha] += 1

    for beta in t:
        if beta not in word_counter or word_counter[beta] == 0:
            return False
        word_counter[beta] -= 1
    return True

# 시간복잡도: O(n)
# 공간복잡도: O(n)

tc_1 = is_anagram("anagram", "nagaram") is True
tc_2 = is_anagram("rat", "car") is False
tc_3 = is_anagram("a", "ab") is False
tc_4 = is_anagram("aacc", "ccac") is False

print('tc_1', tc_1)
print('tc_2', tc_2)
print('tc_3', tc_3)
print('tc_4', tc_4)
