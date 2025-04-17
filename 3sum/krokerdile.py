class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            target = -nums[i]
            seen = set()
            j = i + 1

            while j < n:
                complement = target - nums[j]
                if complement in seen:
                    res.append([nums[i], complement, nums[j]])
                    while j + 1 < n and nums[j] == nums[j+1]:
                        j += 1
                seen.add(nums[j])
                j += 1
        return list(set(tuple(x) for x in res))
    

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)):
            # 중복된 첫 번째 수는 skip
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    # 중복된 두 번째, 세 번째 수 건너뛰기
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif total < 0:
                    left += 1  # 합이 작으면 왼쪽을 오른쪽으로
                else:
                    right -= 1  # 합이 크면 오른쪽을 왼쪽으로

        return result
