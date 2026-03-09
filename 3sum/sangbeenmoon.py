# time : O(n^2)
# space : O(n)
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        answer = []

        for i, num in enumerate(nums):
            # 중복 제거
            if i > 0 and nums[i] == nums[i-1]:
                continue

            target = num * -1
            
            visited = dict()    # 중복 제거
            left = i + 1
            right = len(nums) - 1

            while left < right:
                sum = nums[left] + nums[right]
                if sum < target:
                    left = left + 1
                elif sum > target:
                    right = right - 1
                else:
                    if nums[left] not in visited:     # 중복 제거
                        answer.append([num, nums[left], nums[right]])
                        visited[nums[left]] = True

                    left = left + 1
                    right = right - 1
        return answer