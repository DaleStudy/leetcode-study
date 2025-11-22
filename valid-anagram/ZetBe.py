'''
문제: 두 문자열이 주어졌을 때, 두 문자열이 아나그램인지 판별하는 함수를 작성하시오.
아나그램이란, 한 문자열의 문자를 재배열하여 다른 문자열을 만들 수 있는 경우를 말합니다. 예를 들어, "listen"과 "silent"는 아나그램입니다.
해결: 딕테이션을 활용하여 각 문자열의 문자 빈도수를 저장한 후, 두 딕테이션이 동일한지 비교합니다.

시간복잡도: O(n), n은 문자열의 길이
각 문자열을 한 번씩 순회하며 딕테이션에 문자의 빈도수를 기록하기 때문에 전체 시간복잡도는 O(n)입니다.
공간복잡도: O(1)
알파벳의 개수는 고정되어 있으므로, 딕테이션에 저장되는 문자의 개수는 최대 26개(영어 알파벳 기준)로 제한됩니다. 따라서 공간복잡도는 O(1)입니다.
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = {}
        d2 = {}
        if len(s) != len(t):
            return False 

        for i in range(len(s)):
            if s[i] in d1:
                d1[s[i]] += 1
            else:
                d1[s[i]] = 1

            if t[i] in d2:
                d2[t[i]] += 1
            else:
                d2[t[i]] = 1

        
        if d1 == d2:
            return True
        return False

