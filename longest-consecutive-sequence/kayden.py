# 시간복잡도: O(N)
# 공간복잡도: O(N)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        answer = 0

        for num in nums:
            if num - 1 not in nums:
                length = 1

                while num + length in nums:
                    length += 1

                answer = max(answer, length)

        return answer
