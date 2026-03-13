import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        """반복되는 횟수가 높은 순으로 Top k인 숫자들을 찾는 함수
        
        방법
        1. 전체 목록을 순회하면서, 각 숫자가 몇 번 나오는지 세어, dict map 만들기.
            이후 value 값 기준으로 정렬해, 상위 k개를 반환하는 방법 => O(n) + O(n log n) => O(n log n)
        2. 1번의 방법에서 dict map을 만드는 걸, python 내장 모듈인 Counter로 대체하기.
            Counter가 약간 더 빠름; C implementation이기 때문.
        3. 1번 방법의 sorted 대신, heapq 모듈의 nlargest 함수를 이용하기. 
            전체 목록을 순회하지 않고, top k에 해당하는 값만 파악하기에 효율적임. O(n) + O(n log k) => O(n log k)
        4. quick select 알고리즘. O(n) + O(n) => O(n); 해당 문제에 구현하지 못함.

        Args:
            nums (list[int]): 정렬되지 않은 중복 포함 정수 배열
            k (int): Top k의 개수

        Returns:
            list[int]: Top k에 해당하는 숫자들의 리스트
        """
        if len(nums) <= 1:
            return nums
        count = Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.get)
