"""
복잡도 : 예상 -> 예상한 이유

시간 복잡도 : O(n) -> 배열의 길이 만큼 연산하기 때문
공간 복잡도 : O(1)? -> 생성한 count_list 배열이 상수이기 때문
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_list = [0] * 26
        for s_char in s:
            count_list[ord(s_char) - ord('a')] += 1
        for t_char in t:
            count_list[ord(t_char) - ord('a')] -= 1
        for count in count_list:
            if count != 0:
                return False
        return True

