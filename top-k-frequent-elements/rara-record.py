from typing import List
from heapq import nlargest

"""
문제 설명:
이 문제는 주어진 k번째 만큼 빈도수가 높은 값들을 반환하는 문제
빈도수 체크 후, 반환 값 순서는 상관 없다고 했으니 heap 사용

{
  1: 3,  # 1이 3번 등장
  2: 2,  # 2가 2번 등장
  3: 1,  # 3이 1번 등장
}

빈도수 기준으로 k번째만큼 큰 값을 반환
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dic = {}

        for num in nums:
            if num in count_dic:
                count_dic[num] += 1
            else:
                count_dic[num] = 1

        # 빈도수가 큰 순서대로 k개를 반환
        return nlargest(k, count_dic, key=count_dic.get)

"""
시간복잡도: O(n log k)
- 딕셔너리 O(n) + heap을 사용해서 k번째 요소까지 반환 O(n log k) = O(n log k)

공간복잡도: O(n)
- 최대 n개의 서로 다른 숫자가 있을 수 있고, O(n)
- heap은 최대 k개만 저장 -> O(k)
전체적으로 O(n)
"""




