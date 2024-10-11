class Solution:
    # 시간복잡도: O(N)
    # 공간복잡도: O(1)
    def maxSubArray(self, nums: List[int]) -> int:

        prev = 0
        answer = float('-inf')
        for num in nums:
            if prev + num > num:
                prev += num
            else:
                prev = num
            answer = max(answer, prev)

        return max(prev, answer)
