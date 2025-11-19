class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list = sorted(list(s))
        t_list = sorted(list(t))
        # 1. 두 단어의 길이가 다른 경우 false 반환
        if len(s_list) != len(t_list):
            return False
        else:
            # 2. 각 알파벳의 순서가 일치하지 않는 경우 false 반환
            for i in range(0, len(s_list)):
                if s_list[i] != t_list[i]:
                    return False
            return True
