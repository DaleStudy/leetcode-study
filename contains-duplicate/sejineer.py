"""
시간 복잡도 O(n)
공간 복잡도 O(n)

코드 가독성 향상 코드
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
"""
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        check = set([])
        for i in nums:
            if i not in check:
                check.add(i)
            else:
                return True
        return False
