"""TC: O(n log n), SC: O(n)

1
nums를 순회하면서 dict를 채우는 데에 TC: O(n), SC: O(n)
* 단, dict에서 `Set Item` 할때
    Amortized Worst Case O(n) 말고
    Average Case O(1) 적용 가정

2
ref: https://docs.python.org/3/library/collections.html#collections.Counter
A Counter is a dict subclass for counting hashable objects.

Counter, 즉, dict의 (값, 키) 튜플을 sorting하는 데에 TC: O(n log n), SC: O(n)
* 이때 값이 클수록 앞에 오게 하기 위해 값을 음수로 바꿔줬다.

3
sorted된 리스트에서 튜플의 두 번째 아이템만 뽑은 다음에
리스트의 앞 k개의 아이템 리턴.
"""

from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], n: int) -> List[int]:
        return [i for _, i in sorted([(-v, k) for k, v in Counter(nums).items()])][:n]
