class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        first = len(nums) # O(1) : 리스트 객체는 이미 자기자신의 길이를 저장하고 있음
        set_nums = set(nums) # O(N)
        second = len(set_nums)
        return (first != second)

# 시간 복잡도 : O(N)
