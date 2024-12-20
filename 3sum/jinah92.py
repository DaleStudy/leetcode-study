# 공간복잡도 : O(1), 시간복잡도 : O(N^2)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        three_sums = set()
        nums.sort()

        for i in range(len(nums)-2):
            low, high = i + 1, len(nums)-1
            while low < high:
                three_sum = nums[i] + nums[high] + nums[low]
                if three_sum < 0:
                    low += 1
                elif three_sum > 0:
                    high -= 1
                else:
                    three_sums.add((nums[i], nums[high], nums[low]))
                    low, high = low+1, high-1
            
        return list(three_sums)

                