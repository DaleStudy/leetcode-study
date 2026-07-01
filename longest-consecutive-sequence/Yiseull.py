class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        answer = 0
        numsSet = set(nums)
        for num in numsSet:
            if num - 1 in numsSet:
                continue

            size = 1
            while num + 1 in numsSet:
                size += 1
                num += 1

            answer = max(answer, size)

        return answer
