class Solution:
    # Space complexity: O(n)
    # Time complexity: O(n)
    def naive(self, nums: list[int]) -> list[int]:
        prefix = [1]
        for num in nums[:-1]:
            prefix.append(prefix[-1] * num)

        reverse_nums = nums[::-1]        
        postfix = [1]
        for num in reverse_nums[:-1]:
            postfix.append(postfix[-1] * num)
        postfix = postfix[::-1]

        return [prefix[i] * postfix[i] for i in range(len(nums))]

    # Space complexity: O(1)
    # Time complexity: O(n)
    def with_constant_space(self, nums: list[int]) -> list[int]:
        n = len(nums)
        answer = [1] * n

        # 1. save prefix product to temp 
        temp = 1
        for i in range(1, n):
            temp *= nums[i - 1]
            answer[i] *= temp 

        # 2. save postfix product to temp 
        temp = 1
        for i in range(n - 2, -1, -1):
            temp *= nums[i + 1]
            answer[i] *= temp

        return answer


    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # index -> product
        # 0 ->  - [1, 2, 3] 
        # 1 -> [0] - [2, 3]
        # 2 -> [0, 1] - [3] 
        # 3 -> [0, 1, 2] -
        return self.with_constant_space(nums)
        

