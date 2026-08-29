class Solution:
    # Time Complexity: O(n*log(n)), n: len(nums)
    # Space Complexity: O(n), n: len(nums)
    def lengthOfLIS(self, nums: List[int]) -> int:
        seq = []

        for num in nums:
            if not seq or (seq[-1] < num):
                seq.append(num)
                continue

            # overwrite the smaller value with binary search
            left, right = 0, len(seq)
            while left < right:
                mid = (left + right) // 2
                if seq[mid] < num:
                    left = mid + 1
                else:
                    right = mid

            seq[left] = num

        return len(seq)
