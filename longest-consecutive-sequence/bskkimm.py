from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0

        dict_consecutive = defaultdict(int)
        group_num = 0 # consecutive group number

        dict_consecutive[group_num] += 1 # w.r.t the first num of nums

        # sort in the ascending order eliminating duplicates
        nums = sorted(set(nums))

        # 2. build dict_consecutive
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] == 1:
                dict_consecutive[group_num] += 1
            else:
                group_num += 1
                dict_consecutive[group_num] += 1
        
        # 3. Get the longest group
        longest_consecutive = max(list(dict_consecutive.values()))

        return longest_consecutive
