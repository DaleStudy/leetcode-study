class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """O(nlogn) complexity"""
        frequency = defaultdict(int)
        for n in nums:
            frequency[n] += 1
        sorted_frequency = sorted(frequency.items(), key=lambda x:x[1], reverse=True)
        answer = []
        for i in range(k):
            answer.append(sorted_frequency[i][0])
        return answer
