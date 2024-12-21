class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Naive Solution
        # Tc : O(n^3) / Sc : O(nC_3)
        
        n = len(nums)
        """
        for i in range(n-2):
            for j in range(i+1,n-1):
                for k in range(j+1, n):
                    if nums[i]+nums[j]+nums[k] == 0:
                        ret.add(tuple(sorted([nums[i], nums[j], nums[k]])))

        ret = [x for x in ret]
        return ret 
        """

        # Better Solution
        # two-sum question with fixed num (traversal in for loop)
        # Tc : O(n^2) / Sc : O(n)
        ret = []
        nums.sort()

        for i in range(n):
            if i>0 and nums[i] == nums[i-1]:
                continue
            j, k = i+1, n-1

            while j < k:
                sum_ = nums[i] + nums[j] + nums[k]
                if sum_ < 0 : j += 1
                elif sum_ > 0 : k -= 1
                else:
                    ret.append([nums[i], nums[j], nums[k]])
                    j += 1
                
                    while nums[j] == nums[j-1] and j<k:
                        j += 1
            
        return ret

