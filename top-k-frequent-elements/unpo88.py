from collections import Counter


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        nums_count = Counter(nums)
        return [key for key, _ in nums_count.most_common(k)]

""" 
================================================================================
풀이 과정
================================================================================

[1차 시도] Counter의 most_common() 활용
────────────────────────────────────────────────────────────────────────────────
1. k개의 빈도가 가장 높은 요소?
2. Counter 함수를 이용해서 K개 개수를 세면 될듯?

        nums_count = Counter(nums)
        return [key for key, _ in nums_count.most_common(k)]

[성능 분석]
3. Counter.most_common() 메서드는 내부는 어떻게 구현되어있지?


    def most_common(self, n=None):
        '''List the n most common elements and their counts from the most
        common to the least.  If n is None, then list all element counts.

        >>> Counter('abracadabra').most_common(3)
        [('a', 5), ('b', 2), ('r', 2)]

        '''
        # Emulate Bag.sortedByCount from Smalltalk
        if n is None:
            return sorted(self.items(), key=_itemgetter(1), reverse=True)

        # Lazy import to speedup Python startup time
        import heapq
        return heapq.nlargest(n, self.items(), key=_itemgetter(1))

4. n이 없으면 모든 요소를 빈도수 순서대로 반환
5. Heap 기반 알고리즘을 사용하고 있네? (Min Heap)
6. _itemgetter(1)은 카운트를 기준으로 정렬하기 위한 것
"""
