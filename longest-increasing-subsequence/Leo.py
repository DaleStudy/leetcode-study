class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        arr = [nums.pop(0)]

        for n in nums:
            if n > arr[-1]:
                arr.append(n)
            else:
                arr[bisect_left(arr, n)] = n

        return len(arr)

        ## TC: O(nlogn) SC: O(n)

        # if not nums:
        #     return 0

        # n = len(nums)
        # LIS = [1] * n

        # for i in range(1, n):
        #     for j in range(i):
        #         if nums[i] > nums[j]:
        #             LIS[i] = max(LIS[i], 1 + LIS[j])

        # return max(LIS)

        ## DP solution: TC: O(n^2) O(n)
