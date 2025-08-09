class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # O(n)

        n = len(nums)
        result = []

        for i in range(n - 2):
            # target을 잡을때도 이전에 구했다면 패스
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = - nums[i]
            left, right = i + 1, n - 1

            while left < right:
                two_sum = nums[left] + nums[right]

                if two_sum == target:
                    result.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif two_sum < target:
                    left += 1
                else:
                    right -= 1

        return result
