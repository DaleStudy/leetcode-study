# 회전된 오름차순 배열에서 최소값을 이진 탐색으로 찾아라

# O(N) time, O(1) space -> 시간 복잡도 충족 x
class Solution:
    def findMin(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                return nums[i]
        return nums[0]
    

class Solution:


# 이진 탐색 풀이
# O(log n) time, O(1) space
class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 1, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            if nums[0] < nums[mid]:
                low = mid + 1
            else:
                high = mid - 1
        return nums[0]
