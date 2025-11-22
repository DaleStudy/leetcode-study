# 시간 복잡도
# 입력 list를 정렬해서 사용 -> 최대 O(n log n)
# 공간 복잡도
# 입력 list를 set으로 변환 -> 최대 O(n)

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        sorted_nums = list(sorted(set(nums)))
        temp = 1
        result = 0
        # print(sorted_nums)
        for i in range(0, len(sorted_nums) - 1):
            if sorted_nums[i] + 1 == sorted_nums[i+1]:
                temp += 1
            else:
                result = max(result, temp)
                temp = 1
        result = max(result, temp)
        return result
