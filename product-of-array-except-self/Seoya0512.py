'''
Approach
- 배열에 0이 2개 이상 있는 경우, 모든 원소는 0이 되므로 바로 답을 반환
- "self(전체 곱에서 제외될 값)"의 인덱스를 기준으로 왼쪽(before)과 오른쪽(after)곱을 미리 계산해서 배열에 저장
- 최종적으로 before와 after 배열의 같은 인덱스 값을 곱해서 반환

Time Complexity: O(N)
- after, before 배열을 각각 한 번씩 순회하며 계산
- 결과를 반환할때 두 배열을 곱을 계산
Space Complexity: O(N)
- N은 num의 길이이며 N크기에 비례하는 before, after 배열 생성 공간
'''
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums.count(0) > 1:
            return [0] * len(nums)
        
        before = [1] * len(nums)  
        for idx in range(len(nums)-1):
            before[idx+1] = before[idx] * nums[idx]
        
        after = [1] * len(nums)
        for jdx in range(len(nums)-1, 0, -1):
            after[jdx-1] = after[jdx] * nums[jdx]
        
        return [x * y for x, y in zip(before, after)]
