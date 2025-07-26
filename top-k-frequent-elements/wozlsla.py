import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        table = {}  # 1. Initialize

        # 2. Populate frequency map
        for i in range(len(nums)):
            table[nums[i]] = table.get(nums[i], 0) + 1

        # 3. Find top K frequent elements
        topk = heapq.nlargest(k, table, key=table.get)
        return topk


"""
* 초기 아이디어 *
- 하나씩 전부 돌면서 빈도수 저장, k개 만큼만 -> 비교/정렬 과정 고려 필요
- count 함수를 써서 비교후 저장 -> 더 많은 반복? O
- 일단 한번은 다 돌아야함. 가장 적게 돌 수 있는 방법?
- 전체 순차 비교?
- Counter, 빈도수 + top K개

Time complexity : O(N + MlogK)
- step 2 (iteration) : O(N)
  - 리스트의 길이가 N 일때, nums 모두 순회
- step 3 (iteration) : O(NlogK)
  - heapq.nlargest 함수는 table의 모든 M개의 요소(키-값 쌍)를 순회하며, 크기 k의 최소 힙을 유지
  - 힙에 삽입(or 제거 후 삽입) 연산은 힙의 크기 k에 비례, O(logK)
  - 각 요소에 적용 O(MlogK), 최악의 경우 O(NlogK). M은 N을 초과할 수 없음.
  
Space Complexity)
- 빈도수 맵 (딕셔너리): O(N) (최악의 경우, 모든 숫자가 고유할 때)
- 힙 (heapq.nlargest 내부에서 사용): O(K)

* heapq.nlargest *
- 가장 큰 k개의 요소를 찾는 함수  
  1. 힙 초기화. 크기가 k인 (최소)힙 생성
  2. 순회 및 힙 관리
    - table 전체를 순회하며 key=table.get 값을 기준으로 비교
    - 힙이 k개 미만일 경우 요소 추가, 다 찼을경우 비교후 재정렬
      - 현재 요소 b의 값과 힙의 루트에 있는 요소 a를 비교
      - b > a 이면, a를 제거하고 b를 추가 및 재정렬
      - b <= a 이면, b를 버림
    - 힙에 있는 요소들을 정렬된 리스트로 반환
- max heap이 아닌 min heap을 사용하는 이유
"""
