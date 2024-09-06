# 시간복잡도: O(N)
# 공간복잡도: O(1)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        positive, negative = 0, 0

        if nums[0] > 0:
            positive = nums[0]
        else:
            negative = nums[0]

        answer = max(nums)

        for i in range(1, n):
            if nums[i] >= 0:
                positive *= nums[i]
                negative *= nums[i]

                if positive == 0:
                    positive = nums[i]

            else:
                temp = positive
                positive = negative * nums[i]
                negative = temp * nums[i]

                if negative == 0:
                    negative = nums[i]

            answer = max(answer, positive)

        return answer
