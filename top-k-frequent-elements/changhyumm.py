class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = dict()
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        result = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        ans = []
        idx = 0
        while k > 0:
            ans.append(result[idx][0])
            idx += 1
            k -= 1
        return ans
