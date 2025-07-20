"""
    - Time Complexity
        - 바깥 for 루프는 n - 1번, 안쪽 루프는 최대 n - i - 1번 실행
        - 전체적으로 O(n^2)의 시간 복잡도를 가짐짐
    
    - Space Complexity
        - 별도의 자료구조를 사용하지 않음
        - 변수 i, j 그리고 리턴 시 사용하는 [i, j]만 존재
        - 따라서 O(1)의 공간 복잡도를 가짐짐
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
