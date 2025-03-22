'''
시간 복잡도: O(log n)
- 이진 탐색을 사용하여 매 반복마다 검색 범위를 절반으로 줄이므로 O(log n)입니다.

공간 복잡도: O(1)
- 추가적인 배열이나 리스트를 사용하지 않고, 몇 개의 변수만 사용하므로 O(1)입니다.
'''

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:  
                left = mid + 1  # 최소값이 오른쪽에 있음
            else:
                right = mid  # 최소값이 mid 또는 왼쪽에 있음
        
        return nums[left]
