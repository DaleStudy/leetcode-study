"""
Time complexity O(n)
Space complexity O(n)

Prefix sum 
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = [1]
        reverse_products = [1]

        tmp = 1
        for n in nums[:-1]:
            tmp *= n
            products.append(tmp)
        tmp = 1
        for n in nums[::-1][:-1]:
            tmp *= n
            reverse_products.append(tmp)

        answer = [
            products[i] * reverse_products[-i-1]
            for i in range(len(nums))
        ]
        return answer
