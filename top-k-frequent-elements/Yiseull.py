from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # return [key for key, counter in Counter(nums).most_common(k)]

        # counter = {}
        # for num in nums:
        #     if num in counter:
        #         counter[num] += 1
        #         continue
        #     counter[num] = 1
        #
        # return [key for key, counter in sorted(counter.items(), key=lambda x: -x[1])[0:k]]

        counter = {}
        for num in nums:
            if num in counter:
                counter[num] += 1
                continue
            counter[num] = 1

        heap = [(-v, k) for k, v in counter.items()]
        heapify(heap)

        answer = []
        for _ in range(k):
            answer.append(heappop(heap)[1])

        return answer
