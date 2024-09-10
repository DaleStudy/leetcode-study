class Solution:

    # 해시맵
    # 시간복잡도: O(N^2)
    # 공간복잡도: O(N)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()

        check = {}
        for idx, num in enumerate(nums):
            check[num] = idx

        answer = set()
        for i in range(n-2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i + 1, n):
                target = -(nums[i] + nums[j])
                if not check.get(target, None):
                    continue
                if j >= check[target]:
                    continue

                answer.add((nums[i], nums[j], target))

        return list(answer)

    # 투포인터
    # 시간복잡도: O(N^2)
    # 공간복잡도: O(N)
    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()

        answer = set()
        for i in range(n-2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, n-1
            while l<r:
                if nums[l] + nums[r] == -nums[i]:
                    answer.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1

                if nums[l] + nums[r] < -nums[i]:
                    l += 1

                if nums[l] + nums[r] > -nums[i]:
                    r -= 1

        return list(answer)
