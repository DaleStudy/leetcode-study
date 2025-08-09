'''
풀이:
- t 기준 for loop 돌리고 visited 배열 만들어서 s의 모든 곳을 방문하게 함
- t 안의 문자가 s에 없고 visited 가 False 인 경우 -> visited 배열 True로 변경
- but) 중복 문자가 있는 경우 index 사용에 한계가 있음
- so) t의 문자가 s에 있는 경우 해당 문자를 s 배열에서 탈락시킴

시간 복잡도: O(n^2)
- for loop -> O(n)
- digit in list -> 최악의 경우 O(n)
- 최악의 경우 O(n^2)

공간 복잡도: O(n)
- s 문자열을 리스트로 만듬 -> 문자열 크기는 입력됨 = n -> O(n)
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l = list(s)
        for d in t:
            if d in s and d in l:
                l.remove(d)
            else:
                return False

        if not l:
            return True
        else:
            return False
