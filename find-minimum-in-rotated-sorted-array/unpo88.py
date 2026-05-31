class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        
        return nums[left]

"""
================================================================================
풀이 과정
================================================================================

[1차 시도] 이진 탐색 적용 - 기본 구조
────────────────────────────────────────────────────────────────────────────────
1. log(n) 시간 복잡도를 만족시키는 이진 탐색 구조로 최소값을 찾으면 될 것 같음

        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]

2. 시간복잡도: O(log n) - 이진 탐색
3. 공간복잡도: O(1) - 추가 공간 사용 안 함
"""
