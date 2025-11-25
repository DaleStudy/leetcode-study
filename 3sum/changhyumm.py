class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # ans = set()
        # for i in range(len(n)):
        #     seen = {}
        #     for j in range(i+1, len(n)):
        #         complement = -(nums[i] + nums[j])
        #         if complement in seen:
        #             ans.add(tuple(sorted([nums[i], nums[j], complement])))
        #         seen[nums[j]] = j
        # return [list(triplet) for triplet in ans]
        # hash + 이중 loop -> O(n^2)


        ## 투포인터 활용
        # sort + loop -> O(nlogn)
        ans_set = set()
        nums.sort()
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    # 중복제거
                    ans_set.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
        return list(ans_set)
