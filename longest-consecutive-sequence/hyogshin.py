class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        s = set(nums)
        nums = sorted(list(s))
        rs = []
        cnt = 1

        for i in range(len(nums)-1):
            if (nums[i] + 1) == nums[i+1]:
                cnt += 1
            else:
                rs.append(cnt)
                cnt = 1

        rs.append(cnt)
        return max(rs)
        
'''
시간 복잡도: O(n log n)
- set(nums) -> O(n)
- sorted(list(s)) -> O(n log n)
- for loop -> O(n)
- O(2n) + O(n log n) => O(2n) 이 아니라 왜 O(n log n) 이지?

공간 복잡도: O(n)
- set -> O(n)
- sorted() -> O(n)
- rs -> O(n)
- O(3n) => O(n)
'''
