from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
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