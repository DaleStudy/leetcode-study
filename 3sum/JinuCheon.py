# brute force 로 풀어본 답안. O(n3) 다. 역시 timeout.
# dic, set 자료형 익히기 겸 해봤다. 파이썬 편하다 최고.
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        result = set()

        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if (i == j or j == k or i == k):
                        continue
                    if (nums[i] + nums[j] + nums[k] == 0):
                        result.add(tuple(sorted([nums[i], nums[j], nums[k]])))
        
        return list(result)

# LLM 에게 힌트 얻어서 진행.
# i != j, i != k, j != k 조건 때문에 정렬을 하면 안된다고 착각하고 있었다. 사실 고정된 순서는 중요하지 않음.
# 정렬을 진행하고, two pointer 로 진행.
# 통과!
class Solution2:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # 정렬
        nums.sort()
        n = len(nums)
        result = set()

        for i in range(n):
            # i 자리 중복 skip (이전 원소와 같으면 건너뜀)
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # i + left + right === 0 이 되어야 함.
            left = i + 1
            right = n - 1

            while left < right:
                if nums[left] + nums[right] == -nums[i]:
                    result.add(tuple([nums[i], nums[left], nums[right]]))
                    left += 1
                    right -= 1

                elif nums[left] + nums[right] < -nums[i]:
                    left += 1
                else:
                    right -= 1

        return list(result)

# LLM의 피드백.
# 중복을 스킵하는 효율적인 방법이 있었음.
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        result = []

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            if nums[i] > 0:
                break

            left, right = i + 1, n - 1
            target = -nums[i]

            while left < right:
                s = nums[left] + nums[right]
                if s == target:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    
                    # left, right 자리도 중복 skip
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                        
                elif s < target:
                    left += 1
                else:
                    right -= 1

        return result
