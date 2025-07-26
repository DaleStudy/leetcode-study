class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == len(set(nums)):
            return False
        else:
            return True



'''
시간 복잡도: O(n)??
공간 복잡도: set을 활용해 nums 리스트를 복사함 -> len(nums)의 2배?
'''
