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
시간 복잡도: O(1)
- for loop -> 보통 O(n) 이지만, 길이 10001 짜리 고정 배열 -> O(1)로 취급 가능

공간 복잡도: 입력 제외 -> O(1), 입력 포함 -> O(n)
- plus 배열: 10001 -> O(1)
- minus 배열: 10001 -> O(1)
- ans 배열: 길이 k -> O(k)
'''
