class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """
        O(N^2)
        """
        cntr = Counter(nums)

        ans = []

        # First case -> [0, 0, 0] Triplet
        if cntr[0] >= 3:
            ans.append([0, 0, 0])

        # Second case -> two same numbers + one diff number
        for k, v in cntr.items():
            if k == 0:
                continue
            if v >= 2 and -(k * 2) in cntr:
                ans.append([k, k, -(k * 2)])

        s = set(nums)
        nums = list(s)
        nums.sort()

        pos = {k: v for v, k in enumerate(nums)}
        N = len(nums)

        # Third case -> all different numbers
        for i in range(N - 2):
            for j in range(i + 1, N - 1):
                target = -(nums[i] + nums[j])
                if target in pos:
                    k = pos[target]
                    if k > j:
                        ans.append([nums[i], nums[j], nums[k]])

        return ans
