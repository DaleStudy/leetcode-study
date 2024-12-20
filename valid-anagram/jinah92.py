# 공간복잡도: O(n), 시간복잡도: O(n)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_set_1, char_set_2 = {}, {}
        
        for ch in s:
            char_set_1[ch] = 0 if ch not in char_set_1 else char_set_1[ch] + 1
            
        for ch in t:
            char_set_2[ch] = 0 if ch not in char_set_2 else char_set_2[ch] + 1

        # dictionary의 모든 요소 종류와 개수가 일치해야 함
        return char_set_1 == char_set_2
