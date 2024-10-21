class Solution:
    # 시간복잡도: O(logN)
    # 공간복잡도: O(1)
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        st, en = 0, n-1
        while st <= en:
            mid = (st+en)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[st]:
                if nums[st] <= target <= nums[mid]:
                    en = mid - 1
                else:
                    st = mid + 1
            else:
                if nums[mid] <= target <= nums[en]:
                    st = mid + 1
                else:
                    en = mid - 1

        return -1
