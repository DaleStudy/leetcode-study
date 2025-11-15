# 시간 복잡도
# 입력 list를 set으로 변환 -> 최대 O(n)
# 공간 복잡도
# 입력 list를 set으로 변환 -> 최대 O(n)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set_nums = set(nums)
        list_nums = list(set_nums)
        if len(nums) != len(list_nums):
            return True
        else:
            return False
