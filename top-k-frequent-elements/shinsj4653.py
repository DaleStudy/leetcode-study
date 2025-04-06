"""
Constraints:

1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
k is in the range [1, the number of unique elements in the array].

nums 배열에서 원소들의 빈도수 중, 가장 빈도수가 높은 k개의 수들 반환

Time Complexity: O(klogn)

내부적으로 정렬되는 O(logn)을 가지는 최소 힙 사용?

우선 빈도수 사전에 기록 -> dict[숫자] = 빈도수 O(n)
그 다음, 사전.items() 돌면서 heap 에 k개 만큼 넣기 O(k * logn)

k개 만큼 우선순위 큐에 넣기 (-빈도수, 숫자) -> 튜플 넣으면 첫번쨰 원소기준으로 정렬됨

그리고, 나머지 사전.items() 만큼 for i in range(k + 1, n) 만큼만 돌기
-> 만약 힙의 맨 앞 값보다 작으면 넣고, 아니라면 pass

Space Complexity: O(n)

nums만큼 사전에 빈도수 저장

# 간과한 사실
첫 k개만 우선순위 큐에 넣고, 나머지 n - k 만큼 돌때,
힙의 맨 앞 값보다 작거나 같을 때 -> 맨 앞 값을 빼면 안됨!! 그게 정답 수 중 하나일 수 있음


아뿔싸..맨 앞 값만 정렬되어있는 상태라, 마지막 값 반환 시 heappop으로 해줘야할듯!
단순히 for i in range(k) 해서 맨 앞 k 개를 반환하면 정렬되지 않은 상태에서 값을 뽑아내므로 틀릴 수 있음

# 반례

[2,3,4,1,4,0,4,-1,-2,-1]

맨 앞의 값이랑만 비교하다보니, 최대 빈도수 값은 정확히 나오는데 두 번째 이후 값이 첫 번째 값보다 작지 않아서 힙에 못 들어온다..
그래서, 맨 앞의 값 비교 로직 없앰!!

하지만, 힙 내 원소를 k개를 유지 못해서 정렬 시간이 log N 이 되어버림..
-> heap의 사이즈를 k로 유지하면서 작은 빈도 수부터 제거하면,
결국 heap 안에는 가장 많이 등장한 k개의 원소만 남는다.
"""

from collections import defaultdict
from heapq import heappush, heappop


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = defaultdict(int)
        min_heap = []
        ret = []

        for n in nums:
            freq_dict[n] += 1

        for key, value in freq_dict.items():
            heappush(min_heap, (value, key))
            if len(min_heap) > k:
                heappop(min_heap)

        for _ in range(k):
            ret.append(heappop(min_heap)[1])

        return ret
