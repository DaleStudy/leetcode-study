class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        plus = [0] * (10**4 + 1)
        minus = [0] * (10**4 + 1)

        for i in range(len(nums)):
            if nums[i] < 0:
                minus[-(nums[i])] += 1
            else:
                plus[nums[i]] += 1

        ans = []
        for i in range(k):
            if max(max(minus), max(plus)) == max(plus):
                idx = plus.index(max(plus))
                ans.append(idx)
                plus[idx] = 0
            else:
                idx = minus.index(max(minus))
                ans.append(-(idx))
                minus[idx] = 0

        return ans

'''
시간 복잡도: for loop 2회 -> O(2n) -> O(n)
공간 복잡도: 배열 크기 (10**4 + 1) 두 개 + nums 리스트 + ans 배열
'''
