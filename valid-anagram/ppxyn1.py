#idea: dictionary
from collections import Counter 

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dic = Counter(sorted(s))
        t_dic = Counter(sorted(t))
        print(s_dic, t_dic)
        return s_dic==t_dic



# Trial and Error
'''
When you call sorted() on a dictionary, it only extracts and sorts the keys,and the values are completely ignored.
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dic = Counter(s)
        t_dic = Counter(t)
        print(s_dic, t_dic)
        return sorted(s_dic)==sorted(t_dic)
'''





