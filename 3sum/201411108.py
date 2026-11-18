# TC: O(n^2), dictionary의 key를 하나 확인하고, 그 이후 key를 한 번 더 확인하기 때문에
# SC: O(n), 최대 n개의 숫자가 dictionary에 저장
# 풀이
#   1. dictionary를 만들어서, 만들 수 있는 조합을 확인하는 방식. 문제는 풀리지만 시간 복잡도가 O(n^2)로 비효율적
from collections import defaultdict

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        nums_dict = defaultdict(int)

        sorted_nums = nums[:]
        sorted_nums.sort()

        for num in sorted_nums:
            nums_dict[num] += 1

        for key in nums_dict:
            sub_result = [key]
            nums_dict[key] -= 1
            for key2 in nums_dict:
                if key2 < key or nums_dict[key2] <= 0:
                    continue
                sub_result.append(key2)
                nums_dict[key2] -= 1
                diff = 0 - sum(sub_result)
                if diff in nums_dict and diff >= key2 and nums_dict[diff] > 0:
                    sub_result.append(diff)
                    result.append(sub_result)
                sub_result = [key]
                nums_dict[key2] += 1
            nums_dict[key] += 1
        
        return result

