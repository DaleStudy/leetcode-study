class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def count_char(target_str):
            dict_char = {}
            for c in target_str:
              dict_char[c] = dict_char.get(c, 0) + 1
            return dict_char

        dict_s = count_char(s)          
        dict_t = count_char(t)

        if dict_s == dict_t:
            return True
        return False
        
