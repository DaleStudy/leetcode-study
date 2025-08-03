from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        len_n = len(nums)
        front_cum = [1] * len_n
        back_cum = [1] * len_n

        for i in range(1, len_n):
            front_cum[i] = front_cum[i - 1] * nums[i - 1]

        for j in range(1, len_n):
            idx = len_n - j - 1
            back_cum[idx] = back_cum[idx + 1] * nums[idx + 1]

        final = [front_cum[i] * back_cum[i] for i in range(len_n)]

        return final
