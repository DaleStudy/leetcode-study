// TC: O(N)
// SC: O(N)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        cnt = Counter(nums)  # TC: O(n)
        freq_map = defaultdict(list)
        freq_max = 0

        for num, freq in cnt.items():
            freq_map[freq].append(num)
            freq_max = max(freq_max, freq)

        ret = []

        for freq in range(freq_max, 0, -1):
            if freq not in freq_map:
                continue

            ret.extend(freq_map[freq])

            if len(ret) >= k:
                break

        return ret

