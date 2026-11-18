# TC: O(n^2), 첫 번째 요소를 기준으로 n - 2번, left와 right를 기준으로 n번 반복 실행
# SC: O(n), 최대 n개
# 풀이
#   1. dictionary를 만들어서, 만들 수 있는 조합을 확인하는 방식
#   2. 정렬 후, 첫 번째 요소를 기준으로 left와 right를 두고 합이 0이 되는 조합을 찾는 방식
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []

        sorted_nums = nums[:]
        sorted_nums.sort()

        for i in range(len(sorted_nums) - 2):
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]: # 이미 확인한 숫자는 continue
                continue

            left = i + 1
            right = len(sorted_nums) - 1

            while left < right:
                total = sorted_nums[i] + sorted_nums[left] + sorted_nums[right]

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([sorted_nums[i], sorted_nums[left], sorted_nums[right]])

                    # 이미 확인한 숫자는 skip
                    while left < right and sorted_nums[left] == sorted_nums[left + 1]:
                        left += 1
                    while left < right and sorted_nums[right] == sorted_nums[right - 1]:
                        right -= 1
                        
                    left += 1
                    right -= 1
                
        return result

