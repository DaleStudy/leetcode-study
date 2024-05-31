class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        res = [1] * length
        ltor = 1
        rtol = 1

        for i in range(length):
            res[i] *= ltor
            ltor = ltor * nums[i]
            res[length - i - 1] *= rtol
            rtol = rtol * nums[length - i - 1]

        return res

        ## TC: O(n), SC: O(1) 
