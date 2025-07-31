from typing import List

# Time Complexity O(n log n)
# - check len first
# - make set for one of list for each values
#   - if there's a duplication, then value += 1. This is a number of count.
# - fetch value using set.get() method.
#   - minus 1 and check if it is less than 0 which means it's invalid. return false directly.
# Space Complexity O(n)
# - when sorting takes O(n)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_list = list(s)
        t_list = list(t)

        if len(s_list) != len(t_list):
            return False

        t_set = {}
        for t_val in t_list:
            cur = t_set.get(t_val, 0)
            cur += 1
            t_set[t_val] = cur
            
        
        flag = True
    
        for s_val in s_list:
            if t_set.get(s_val):
                cur = t_set.get(s_val)
                cur -= 1
                t_set[s_val] = cur
                if cur < 0:
                    flag = False
                    break 
            else:
                flag = False
                break
        
        return flag
    
    # previous logic
        # s_sorted = sorted(s)
        # t_sorted = sorted(t)

        # for i in range(len(s_sorted)):
        #     if s_sorted[i] != t_sorted[i]:
        #         return False
        # return True


if __name__ == "__main__":
    solution = Solution()

    s = "a"
    t = "ab"

    result = solution.isAnagram(s, t)
    print(result)
