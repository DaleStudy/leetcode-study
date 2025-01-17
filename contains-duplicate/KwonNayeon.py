"""
Title: 217. Contains Duplicate  
Link: https://leetcode.com/problems/contains-duplicate/  

Summary:
    - 주어진 배열 `nums`에서 어떤 값이 한 번 이상 등장하면 True를 반환하고, 배열의 모든 값이 유일한 경우에는 False를 반환함
    - Input: `nums = [1,2,3,1]`
    - Output: `True`

Conditions:
    - 중복이 있으면: 배열에서 적어도 하나의 값이 두 번 이상 등장하면 `True` 반환
    - 중복이 없으면: 배열의 모든 값이 유일하면 `False` 반환
"""

"""
First Try
Time Complexity:
    - O(n) * O(n) = O(n^2): `for` 루프에서 `nums.count(i)`를 호출할 때마다 리스트를 순회하므로, 전체 시간 복잡도는 `O(n^2)`
"""
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in nums:
            if nums.count(i) > 1:
                return True
        return False

"""
Second Try (set를 활용하여 이미 본 요소를 효율적으로 추적하는 방법)
Time Complexity:
    - O(n): `for` 루프에서 각 숫자에 대해 `in` 연산과 `add` 연산이 상수 시간 O(1)으로 처리되므로, 전체 시간 복잡도는 O(n)
"""
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False
