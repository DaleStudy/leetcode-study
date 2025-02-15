class Solution:
    """
    Brute Force

    Time: O(n^2)
    Space: O(1)
    """

    def maxProduct(self, nums: List[int]) -> int:

        max_prod = float(-inf)
        for i in range(len(nums)):
            prod = nums[i]
            max_prod = max(max_prod, prod)
            for j in range(i + 1, len(nums)):
                prod *= nums[j]
                max_prod = max(max_prod, prod)

        return max_prod

    """
    최소곱, 최대곱을 모두 저장하면서 최대값을 찾는다.
    (음수 곱 양수곱을 모두 커버하기 위해 최소곱도 저장한다.)
    
    Time: O(n)
    Space: O(1)
    """

    def maxProduct(self, nums: List[int]) -> int:
        result = nums[0]
        min_prod, max_prod = 1, 1
        for num in nums:
            arr = [min_prod * num, max_prod * num, num]
            min_prod = min(arr)
            max_prod = max(arr)
            result = max(max_prod, result)
        return result
