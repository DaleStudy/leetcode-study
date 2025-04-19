from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        Using (min)heap
        [Complexity]
        Time: O(log n)
        Space: O(n+k)
        '''
        from heapq import heappush, heappop
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        heap = []
        for num, freq in counter.items():
            heappush(heap, (freq, num))
            if len(heap) > k:
                heappop(heap)
        return [num for _, num in heap]
        '''
        Using hash table 
        [Complexity]
        Time: O(n log n)
        Space: O(n)
        '''
        '''
        countDict = {}
        for num in nums:
            if num in countDict:
                countDict[num] += 1
            else:
                countDict[num] = 1
        sortedDictList = sorted(countDict.items(), key=lambda item: item[1], reverse = True)
        freqElements = []
        for i in range(k):
            freqElements.append(sortedDictList[i][0])
        return freqElements
        '''
