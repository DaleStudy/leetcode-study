'''
문제: Top K Frequent Elements
nums 배열에서 가장 자주 등장하는 k개의 요소를 반환하라.
풀이: 딕셔너리를 이용하여 각 숫자의 등장 빈도를 저장한 후,
    빈도수를 기준으로 정렬하여 상위 k개의 숫자를 반환한다.

시간복잡도: O(k log k + n) (n은 nums의 길이, k는 반환할 요소의 개수)
    최악의 경우, O(n log n)이 될 수 있지만, k가 작을 때는 O(k log k + n)이 더 적합하다.
공간복잡도: O(n)
    딕셔너리에 각 숫자의 빈도를 저장하는데 O(n)의 공간이 필요하므로 전체 공간복잡도는 O(n)

사용한 자료구조: 딕셔너리, 리스트
'''



import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr = {}
        answ = []
        a = []
        for i in nums:
            if i in arr:
                arr[i] += 1
            else:
                arr[i] = 1
        
        a = sorted(arr.items(), key=lambda x:x[1], reverse=True)
        for i in range(k):
            answ.append(a[i][0])
        return answ

