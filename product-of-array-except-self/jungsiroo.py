class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Solution 1 :모든 수를 미리 곱해두기
        # 0을 포함한다면 미리 0의 개수를 체크해두기

        n = len(nums)
        ret = [0 for _ in range(n)]
        """
        all_product = 1
        non_zero_product = 1
        zero_cnt = 0

        for x in nums:
            all_product *= x

            if x == 0: 
                zero_cnt += 1
            else:
                non_zero_product *= x

        if zero_cnt > 1:
            return ret

        for i in range(n):
            if nums[i] == 0:
                ans = non_zero_product
            else:
                ans = all_product // nums[i]
            ret[i] = ans
        return ret
        """

        # Solution 2 : w/o division
        # prefix sum과 같이 풀이 진행
        # Tc : O(n) / Sc : O(n) - no extra memory

        prefix_pr, postfix_pr = 1, 1
        for i in range(n):
            ret[i] = prefix_pr
            prefix_pr *= nums[i]
        for i in range(n-1, -1, -1):
            ret[i] *= postfix_pr
            postfix_pr *= nums[i]
        return ret
            

