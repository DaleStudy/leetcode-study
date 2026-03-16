from itertools import combinations

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        time complexity : O(n^2)
        space complexity : O(1)
        """
        answer = []
        nums.sort()
        n = len(nums)

        for i in range(n):
            #skipped if nums[i] == nums[i-1] to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i-1]:
                continue

            #search with two pointer
            left, right = i+1, n-1

            while left < right:
                total = nums[left] + nums[i] + nums[right]
                if total == 0:
                    answer.append([nums[left], nums[i], nums[right]])
                    
                    #move the pointers past duplicates
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1

                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return answer
