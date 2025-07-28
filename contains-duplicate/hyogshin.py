class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == len(set(nums)):
            return False
        else:
            return True



'''
시간 복잡도: O(n)
- set(nums)는 내부적으로 nums의 모든 원소에 대해 __hash__() 및 __eq__() 호출 -> O(n)
- len() 함수는 O(1) -> 무시

공간 복잡도: O(n)
- set(nums)는 nums의 원소를 모두 저장할 수 있게 공간 사용 -> 최악의 경우 O(n)
'''
