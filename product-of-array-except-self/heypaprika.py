"""
복잡도 : 예상 -> 예상한 이유

시간 복잡도 : O(n) -> for 문이 여러번 있지만, len(nums)만큼 여러번 반복하므로 O(n)
공간 복잡도 : O(n) -> len(nums)만큼의 배열 하나가 더 생기므로
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros = 0
        products = 1
        ans_list = [0] * len(nums)

        for i in range(len(nums)):
            if nums[i] == 0:
                zeros += 1
            products *= nums[i]

        if zeros == 1:
            products = 1
            alived_i = -1
            for i in range(len(nums)):
                if nums[i] == 0:
                    alived_i = i
                    continue
                products *= nums[i]
            ans_list[alived_i] = products
            return ans_list
        elif zeros >= 2:
            return ans_list

        ans_list = [products] * len(nums)
        for i in range(len(nums)):
            ans_list[i] //= nums[i]

        return ans_list

