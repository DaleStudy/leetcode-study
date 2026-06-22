from collections import Counter 
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         s_dic = Counter(sorted(s))
#         t_dic = Counter(sorted(t))
#         return s_dic==t_dic

# fixed
# do not need to both Counter and sorting 

# Ans 1 (Only Counter)
# Time Complexity: O(N)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dic = Counter(s)
        t_dic = Counter(t)
        return s_dic==t_dic

# Ans 2  (Only Sorting)
# Time Complexity: O(Nlog(N))
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_arr = sorted(s)
        t_arr = sorted(t)
        return s_arr==t_arr

