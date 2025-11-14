
# set에 저장하면서 중복 여부 확인하기
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hashset = set()
        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        return False
