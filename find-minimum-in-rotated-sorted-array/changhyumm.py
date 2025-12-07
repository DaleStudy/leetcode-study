class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 시간복잡도 O(logn) 제약사항이 있으므로 binary search 사용
        left = 0
        right = len(nums) - 1
        # rotated sort 이므로 mid와 right 비교
        # mid 와 left 비교시 최소값이 어딨는지 특정할 수가 없음 (예외케이스 발생)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
        return nums[left]
