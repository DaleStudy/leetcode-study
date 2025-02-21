"""
1) binary search 로 pivot 찾아 2번 binary search 하기
Time: O(log(n))
Space: O(1)
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def find_pivot():
            low, high = 0, len(nums) - 1
            while low <= high:
                mid = (low + high) // 2
                if mid > 0 and nums[mid - 1] >= nums[mid]:
                    return mid
                if nums[0] <= nums[mid]:
                    low = mid + 1
                else:
                    high = mid - 1
            return 0

        def binary_search(low, high):
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    return mid
                if nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return -1

        pivot = find_pivot()

        idx = binary_search(0, pivot - 1)
        return idx if idx > -1 else binary_search(pivot, len(nums) - 1)


"""
2) binary search
    left sorted case
    4 5 6 7 0 1 2 3
        m
        left target case
        right target case

    right sorted case
    6 7 0 1 2 3 4 5
            m
        left target case
        right target case
Time: O(log(n))
Space: O(1)
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if target == nums[mid]:
                return mid

            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1
