class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first = {}
        second = {}

        for c in s:
            if c in first:
                first[c] += 1
            else:
                first[c] = 1
        
        for c in t:
            if c in second:
                second[c] += 1
            else:
                second[c] = 1
        
        return first == second


# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         first = {}

#         if len(s) != len(t):
#             return False

#         for i in range(len(s)):
#             if s[i] in first:
#                 first[s[i]] += 1
#             else:
#                 first[s[i]] = 1

#         for i in range(len(t)):
#             if t[i] in first:
#                 first[t[i]] -= 1
#             else:
#                 return False

#         for i in first.values():
#             if i != 0:
#                 return False

#         return True
