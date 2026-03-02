# https://leetcode.com/problems/two-sum/description/

# class Solution(object):
#     def twoSum(self, nums, target):
#         for i in range(len(nums)):
#             for j in range(len(nums)):
#                 if nums[i]+nums[j] == target:
#                     if i != j:
#                         return [i, j]                    
# > 해당 방식 사용 시 시간 복잡도가 O(n²)이라 개선을 해 보고자 아래 솔루션으로 재풀이 진행

class Solution(object):
    def twoSum(self, nums, target):
        seen = {}

        for i, num in enumerate(nums):
            diff = target - num

            if diff in seen:
                return [seen[diff], i]

            seen[num] = i

# index를 기억하도록 하면 반복문 한번 O(n), 딕셔너리 조회 평균 O(1)로 전체 O(n)이 됨
