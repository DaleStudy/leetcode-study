"""
Inputs: two strings : s, t

Outputs: t 가 s의 anagram인지에 대한 여부

Constraints:

1 <= s.length, t.length <= 5 * 10^4
s and t consist of lowercase English letters.

Time Complexity: O(n)

각 문자들의 등장 횟수만 같으면 되지 않나?

s의 Counter 생성
t의 Counter 생성

t Counter의 keys() 돌면서,
해당 값이 s Counter 배열 key에 있는지, 그리고 그 key의 value값이 서로 같은지 체크

Space Complexity: O(n)

"""

# 첫 코드

from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict, t_dict = defaultdict(int), defaultdict(int)

        for ch in s:
            s_dict[ch] += 1

        for ch in t:
            t_dict[ch] += 1

        for key in t_dict.keys():
            if key not in t_dict or t_dict[key] != s_dict[key]:
                return False

        return True

# 반례 발생

# s = "ab", t = "a"
# 어느 한 문자열을 기준으로 세면 안되는 것 같다
# 두 count 사전을 모두 돌아야할듯. t keys()를 기준으로만 돌면 true가 나와버림. 답은 false인데


from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict, t_dict = defaultdict(int), defaultdict(int)

        for ch in s:
            s_dict[ch] += 1

        for ch in t:
            t_dict[ch] += 1

        for key in t_dict.keys():
            if key not in s_dict or t_dict[key] != s_dict[key]:
                return False

        for key in s_dict.keys():
            if key not in t_dict or t_dict[key] != s_dict[key]:
                return False

        return True

