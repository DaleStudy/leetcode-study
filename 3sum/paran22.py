class Solution:
    # time complexity: O(n^2)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = set()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum == 0:
                    answer.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif sum > 0:
                    right -= 1
                elif sum < 0:
                    left += 1

        return [list(x) for x in answer]



        