class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequent = {}
        for n in nums:
            if n not in frequent:
                frequent[n] = 1
            else:
                frequent[n] += 1

        answer = []
        for f in sorted(frequent.items(), key=lambda item: item[1], reverse=True):
            if k > 0:
                answer.append(f[0])
            k -= 1
        return answer

