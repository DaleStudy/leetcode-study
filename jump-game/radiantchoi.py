class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reachable = [False] * len(nums)
        destination = len(nums) - 1

        for index, strength in list(enumerate(nums))[::-1]:
            if index + strength >= destination:
                reachable[index] = True
                destination = index

        return reachable[0]
