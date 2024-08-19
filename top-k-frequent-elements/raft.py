class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Frequency
        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1
        
        freq_list = []
        for key, val in freq.items():
            freq_list.append((-1 * val, key))
        
        heapq.heapify(freq_list)
        
        res = []
        for _ in range(k):
            res.append(heapq.heappop(freq_list)[1])
        
        return res

    # T: nlogn
    # S: n

    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        res = []
        # Frequency
        count = defaultdict(int)
        for n in nums:
            count[n] += 1

        # Convert to frequency
        frequency = [[] for _ in range(len(nums) + 1)]
        for key, freq in count.items():
            frequency[freq].append(key)

        # top K
        for freq in range(len(nums), 0, -1):
            for n in frequency[freq]:
                res.append(n)

                if len(res) == k:
                    return res
    # T: n
    # S: n

