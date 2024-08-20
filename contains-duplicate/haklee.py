"""TC: O(n)? O(n^2)?, SC: O(n)

ref: https://wiki.python.org/moin/TimeComplexity
set는 dict와 거의 비슷하게 구현되어 있는데,
dict의 `Set Item`의 Average Case는 O(1)이더라도
Amortized Worst Case가 O(n)이다!

즉, set에 아이템을 추가할때마다 해시 충돌이 일어날 경우
최악의 경우 O(n^2)이 걸리므로, 아래의 set(nums)의
TC가 O(n^2)이 되는 것일까..?

set(nums)의 결과가 최악의 경우 SC가 O(n)이다.
"""


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
