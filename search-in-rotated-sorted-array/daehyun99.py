# Time: O(log N)
# Space: O(1)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l+r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        pivot = l
        l, r = 0, len(nums) - 1

        if target >= nums[pivot] and target <= nums[r]:
            l = pivot
        else:
            r = pivot - 1

        while l <= r:
            m = (l+r) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return -1

"""
# Time: O(N)
# Space: O(log N)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def search(l, r):
            if nums[l] == target:
                return l
            if nums[r] == target:
                return r
            if l+1 >= r:
                return -1

            return max(search(l, (l+r)//2), search((l+r)//2, r))

        return search(0, len(nums) - 1)
"""
