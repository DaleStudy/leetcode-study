# TC: O(n), HashMap을 활용하여 알파벳 소문자로 이루어진 문자열의 갯수를 갖고 있기 때문에 O(n)
# SC: O(n), 리스트의 길이가 n
from collections import defaultdict

def convertStrToMap(target: str):
    converted_dict = defaultdict(int)

    for target_char in target:
        converted_dict[target_char] += 1
    
    return converted_dict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False

        s_dict = convertStrToMap(s)
        t_dict = convertStrToMap(t)

        if len(s_dict.keys()) != len(t_dict.keys()):
            return False

        return s_dict == t_dict

