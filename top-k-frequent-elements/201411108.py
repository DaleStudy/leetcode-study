# TC(nlogn), sorted 메서드의 시간 복잡도는 nlogn이다.
# SC(n), k와 nums의 길이가 같을 경우 최악일 것이기 때문에 n일 것이다.
from collections import defaultdict

key = 0
value = 1

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        dictionary = defaultdict(int)

        # O(n)
        for num in nums:
            if num in dictionary:
                dictionary[num] += 1
            else:
                dictionary[num] = 1

        # O(nlogn)
        frequency = sorted(dictionary.items(), key=lambda x: x[value], reverse=True)
        result = []

        for i in range(k):
            result.append(frequency[i][key])
        
        return result

