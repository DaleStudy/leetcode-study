# 문제: https://leetcode.com/problems/contains-duplicate/

# 아이디어:
# 1. nums를 정렬한 다음 [1, len(nums)) 범위를 순회하며, 앞 순서의 번호와 일치하는지 확인한다.
# 2. set 자료구조 사용해서 탐색한 숫자를 기록한다. for문을 돌며 이전에 탐색한 숫자라면 early retrun


# 1) 정렬 사용, 이 경우에는 정렬에 의해 시간 복잡도 O(nlogN), 공간복잡도 O(1)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort() # 정렬에 의해 시간 복잡도 O(nlogN)

        for idx in range(1, len(nums)):
            if nums[idx] == nums[idx-1]:
                return True

        return False


# 2) set 사용, 시간 복잡도 O(N), 공간 복잡도 O(N)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set() # 탐색한 숫자를 기록하는 set

        for n in nums:
            if n in seen:
                return True
            seen.add(n)

        return False
