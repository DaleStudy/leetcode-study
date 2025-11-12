#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sol = {}
        for i in nums:
            sol[i] = sol.get(i, 0) + 1
        
        sorted_items = sorted(sol.items(), key=lambda x: x[1], reverse=True)
        
        ssol = []
        for i in range(k):
            ssol.append(sorted_items[i][0])
        
        return ssol


                

            
        
# @lc code=end

