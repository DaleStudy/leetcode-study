# https://leetcode.com/problems/valid-anagram/description/

# [요구사항]
# 문자열 두 개가 주어졌을 때 애너그램이 맞는지 아닌지를 반환하는 문제
# 애너그램이란? 하나의 단어나 구에 들어 있는 글자들을 모두, 각각 정확히 한 번씩만 사용해서 순서를 바꾸어 만든 다른 단어나 구를 의미한다.
# 두 문자열이 애너그램이면 True, 아니면 False 반환

# [접근법]
# 1. 길이가 다르면 애너그램이 아니므로 바로 False를 반환한다.
# 2. s의 문자 개수를 센 뒤, t를 순회하며 하나씩 차감한다.
# 3. 없는 문자이거나 개수가 부족한 문자를 만나면 False를 반환한다.
# 4. 모든 문자를 정상적으로 처리하면 True를 반환한다.

# Time: O(N)
# Space: O(N)

from collections import Counter

class Solution01:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counter = Counter(s)

        for char in t:
            if counter[char] >= 1:
                counter[char] -= 1
            else:
                return False

        return True

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # 파이썬은 == 로 값을 비교한다.
        # 참조로 비교하려면 is 사용
        return Counter(s) == Counter(t)
