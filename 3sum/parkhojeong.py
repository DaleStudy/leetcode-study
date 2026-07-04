class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result_arr = []
        n = len(nums)
        nums.sort()

        for i in range(n - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = n - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total == 0:
                    result_arr.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1
                elif total > 0:
                    k -= 1
                else:
                    j += 1

        return result_arr
