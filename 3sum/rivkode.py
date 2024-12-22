from typing import List, Tuple, Set

# threeSum3()
# Time Complexity O(n ^ 2)
# - when sorting by sorted function(TimSort) for each string it takes O(nlogn)
# - traversing for loop takes O(n) and check left and right in the while loop at the same time.
# Space Complexity O(n)
# - when sorting takes O(1)


class Solution:
    def threeSum(self, nums: List[int]) -> list[tuple[int, ...]]:

        triplets = set()
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplet = [nums[i], nums[j], nums[k]]
                        triplets.add(tuple(sorted(triplet)))

        return list(triplets)

    def threeSum2(self, nums: List[int]) -> list[tuple[int, ...]]:
        triplets = set()

        for i in range(len(nums)):
            seen = set()
            for j in range(i + 1, len(nums)):
                res = -(nums[i] + nums[j])
                if res in seen:
                    triplet = [nums[i], nums[j], res]
                    triplets.add(tuple(sorted(triplet)))
                seen.add(nums[j])

        return list(triplets)

    def threeSum3(self, nums: List[int]) -> list(tuple[int, ...]):
        triplets = set()
        nums.sort()

        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1

            while l < r:
                res = nums[l] + nums[r] + nums[i]
                if res > 0:
                    r -= 1
                elif res < 0:
                    l += 1
                elif res == 0:
                    triple = (nums[l], nums[r], nums[i])
                    triplets.add(triple)
                    l, r = l + 1, r - 1
                else:
                    raise Exception
        return list(triplets)

if __name__ == "__main__":
    nums = [-1,0,1,2,-1,-4]


    solution = Solution()
    solution.threeSum3(nums)
