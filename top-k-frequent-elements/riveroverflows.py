from typing import List


class Solution:
    """
    풀이:
    - 빈도수 세기 + Bucket Sort를 조합해서 정렬 없이 O(n)에 상위 k개를 뽑는다.
    - 1단계: nums를 순회하며 각 숫자의 등장 횟수를 dict로 센다.
    - 2단계: 빈도수를 인덱스로 하는 버킷 배열을 만든다.
      빈도수는 최대 len(nums)이므로 배열 크기가 고정됨.
    - 3단계: 버킷 배열을 뒤에서부터(높은 빈도수부터) 순회하며 k개를 수집한다.
    - 정렬(O(n log n)) 대신 버킷의 인덱스 자체가 정렬 역할을 하므로 O(n).

    TC: O(n)
      - 빈도수 세기: nums를 한 번 순회. O(n).
      - 버킷 배열 생성: 고유 원소 수만큼 순회. 최악 O(n).
      - 상위 k개 수집: 버킷 배열을 뒤에서부터 순회. 최악 O(n).
      - 종합: O(n).

    SC: O(n)
      - counts(dict): 최악 n개의 고유 원소. O(n).
      - bucket(list of lists): 크기 n+1. O(n).
      - answer(list): 최대 k개. O(k) ≤ O(n).
      - 종합: O(n).
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = dict()
        for num in nums:
            if num not in counts:
                counts[num] = 0
            counts[num] += 1

        bucket = [[] for _ in range(len(nums) + 1)]
        for num, cnt in counts.items():
            bucket[cnt].append(num)

        answer = []
        for cnt_list in reversed(bucket):
            if not cnt_list:
                continue
            for num in cnt_list:
                answer.append(num)
                if len(answer) == k:
                    return answer
