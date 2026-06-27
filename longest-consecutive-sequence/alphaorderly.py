class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0

        s: set[int] = set()
        d: dict[int, int] = {}

        large = -1

        for num in nums:
            s.add(num)

        for num in nums:
            if num not in s:
                continue
            if len(s) == 0:
                break
            streak = 1
            s.remove(num)
            for i in range(num - 1, -(10**9) - 1, -1):
                if i in s:
                    s.remove(i)
                    streak += 1
                    continue
                elif i in d:
                    streak += d[i]
                break
            d[num] = streak
            large = max(large, streak)

        return large
