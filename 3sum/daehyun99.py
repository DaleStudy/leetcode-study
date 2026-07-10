class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0:
                break
            if i > 0 and a == nums[i-1]:
                continue
            
            l, r = i+1, len(nums) - 1
            while l < r:
                total = a + nums[l] + nums[r]
                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res

"""from collections import Counter

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        counts = Counter(nums)
        result: set[tuple[int, int, int]] = set()

        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                adding = -(nums[i] + nums[j])

                if adding not in counts:
                    continue

                local_counts = Counter([nums[i], nums[j], adding])

                for num, count in local_counts.items():
                    if counts[num] < count:
                        break
                else:
                    triplet = tuple(sorted([nums[i], nums[j], adding]))
                    result.add(triplet)

        return [list(triplet) for triplet in result]
"""
