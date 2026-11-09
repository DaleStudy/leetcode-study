# TC: O(n), nums의 원소를 하나씩 확인하기 때문에 O(n), 첫 두 원소가 같다면 O(1)
#           set() 메서드는 C언어로 처리하기 때문에 실제 leetcode 제출 상 속도는 set을 활용한 경우
# SC: O(n), 최악의 경우 n개의 원소가 set에 들어갈 수 있기 때문에 O(n)
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        numsSet = set(nums)

        if (len(numsSet) == len(nums)):
            return False

        return True
    