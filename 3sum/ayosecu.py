from typing import List

class Solution:
    """
        - Algorithm
            - Sort and compares with three pointers: target, left(l), right(r)
        - Time Complexity: O(n^2), n = len(nums)
            - sort : O(nlogn)
            - nested two loops : O(n^2)
            - O(nlogn + n^2) => O(n^2)
        - Space Complexity: O(n^2) if result included.
            - result size : result.append() called in n^2 times (nested two loops)
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        
        n = len(nums)
        for i in range(n - 2):
            # skip duplicated numbers
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            target = nums[i]
            l, r = i + 1, n - 1
            while l < r:
                if nums[l] + nums[r] == -target:
                    result.append([target, nums[l], nums[r]])                   
                    # skip duplicated numbers
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] < -target:
                    l += 1
                else:
                    r -= 1
        
        return result

tc = [
        ([-1,0,1,2,-1,-4], [[-1,-1,2],[-1,0,1]]),
        ([0,1,1], []),
        ([0,0,0], [[0,0,0]])
]

for i, (nums, e) in enumerate(tc, 1):
    sol = Solution()
    r = sol.threeSum(nums)
    print(f"TC {i} is Passed!" if e == r else f"TC {i} is Failed! - Expected: {e}, Result: {r}")
