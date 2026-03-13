# 시간 복잡도: O(n)
# - while문이 이중으로 쓰였지만, nums에 있는 각 요소를 한 번 씩만 탐색하는 풀이임(이미 확인한 요소는 pop/remove로 없애기 때문)
# 공간 복잡도: O(n)
# - set 하나만 사용했기 때문에 길이인 n개만큼만 공간 차지

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_length = 1 if nums else 0  # 빈 배열이 들어올 땐 가장 긴 경우는 0밖에 없음

        while nums:
            num = nums.pop()  # 기준이 될 num을 하나 가져옴
            length = 1
            left, right = 1, 1
            while num - left in nums:
                # 기준 num에서 왼쪽으로 확장 가능한 정도를 계산하여 length를 늘림
                nums.remove(num - left)
                length += 1
                left += 1
            while num + right in nums:
                # 기준 num에서 오른쪽으로 확장 가능한 정도를 계산하여 length를 늘림
                nums.remove(num + right)
                length += 1
                right += 1
            
            max_length = max(max_length, length)  # 기존에 계산해둔 max_length와 비교하여 업데이트

        return max_length
            


# #  ** Other trial
# # 시간 복잡도: O(n log n)
# # - sorting을 했기 때문. 문제 통과는 되지만 문제 내 힌트인 O(n)의 시간복잡도를 충족하진 않음
# # 공간 복잡도: O(n)
# # - nums를 set -> list으로 변환하면서 n개의 개수만큼 저장공간 사용
# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         nums = list(set(nums))
#         if not nums:
#             return 0

#         if len(nums) == 1:
#             return 1

#         nums.sort()
#         max_length = 1 

#         start_i = 0
#         length = 1
#         while start_i < len(nums) - 1 and start_i + length < len(nums):
#             length = 1
#             for i in range(start_i, len(nums) - 1):
#                 if nums[i + 1] == nums[i] + 1:
#                     length += 1
#                 else:
#                     start_i = i + 1
#                     break
#             max_length = max(max_length, length)

#         return max_length
