class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answerSet = set()
        nums.sort()

        for i in range(len(nums) - 2):
            leftIdx = i + 1
            rightIdx = len(nums) - 1
            while leftIdx < rightIdx:
                sum = nums[i] + nums[leftIdx] + nums[rightIdx]
                if sum < 0:
                    leftIdx += 1
                elif sum > 0:
                    rightIdx -= 1
                else:
                    answerSet.add((nums[i], nums[leftIdx], nums[rightIdx]))
                    leftIdx = leftIdx + 1
                    rightIdx = rightIdx - 1

        return list(answerSet)
    
