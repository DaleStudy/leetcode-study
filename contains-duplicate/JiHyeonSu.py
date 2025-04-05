# 중복제거 후 길이 확인 문제
# 시간복잡도 및 공간복잡도 O(n)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))