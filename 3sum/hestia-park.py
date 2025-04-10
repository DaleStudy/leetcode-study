class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer=set()
        for i in range(len(nums)):
            if nums[i] > 0:
                break  # 이후 숫자는 모두 양수 → 합이 0 불가능
            if i > 0 and nums[i] == nums[i - 1]:  
                continue

            left, right = i + 1, len(nums) - 1
            while left < right:
                term = nums[i] + nums[left] + nums[right]
                if term == 0:
                    answer.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif term < 0:
                    left += 1
                else:
                    right -= 1

        return [list(triplet) for triplet in answer]


