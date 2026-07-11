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
                sum_ = nums[left] + nums[right]
                if sum_ < target:
                    left = left + 1
                elif sum_ > target:
                    right = right - 1
                else:
                    if nums[left] not in visited:     # 중복 제거
                        answer.append([num, nums[left], nums[right]])
                        visited[nums[left]] = True

                    left = left + 1
                    right = right - 1
        return answer


# TC : O(n^2)
# SC : O(n)

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        nums.sort()

        answer_map = {}
        answer = []
        
        for i in range(len(nums)):
            target = -1 * nums[i]

            left = i + 1
            right = len(nums) - 1

            while left < right:
                if nums[left] + nums[right] == target:
                    candidate = (target * -1, nums[left], nums[right])
                    if candidate not in answer_map:
                        answer_map[candidate] = True
                        answer.append([target * -1, nums[left], nums[right]])
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    right -= 1
        return answer
                
