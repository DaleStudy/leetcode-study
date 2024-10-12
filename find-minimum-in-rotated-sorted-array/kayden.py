class Solution:
    # 시간복잡도: O(logN)
    # 공간복잡도: O(1)
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        st, en = 0, n-1
        while st < en:
            mid = (st+en)//2
            if nums[mid] > nums[en]:
                st = mid + 1
            else:
                en = mid

        return nums[st]
