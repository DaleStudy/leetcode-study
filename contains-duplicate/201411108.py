# TC: O(n), nums의 원소를 하나씩 확인하기 때문에 O(n)
# SC: O(n), 최악의 경우 n개의 원소가 set에 들어갈 수 있기 때문에 O(n)
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        numSet = set(nums)

        if (len(numSet) == len(nums)):
            return False

        return True
    