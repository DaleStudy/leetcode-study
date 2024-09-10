"""TC: O(n), SC: O(n)

아이디어:
- [0, ..., n]에서 한 숫자만 빠져있는 상황.
- [0, ..., n]을 set으로 만든 다음 특정 숫자가 이 set에 있는지 체크하면 된다.
- 그런데 그렇게 구현하나 위 set에서 set(nums)를 빼고 남은 숫자를 취하나 최악의 경우
  같은 성능이 나올테니 더 코드가 짧아지도록 후자의 방식으로 구현해보자.


SC:
- [0, ..., n]으로 set을 만드는 데에 O(n).
- set(nums)에서 O(n).
- 총 O(n).

TC:
- [0, ..., n]으로 set을 만드는 데에 O(n).
- set(nums)에서 O(n).
- set에 difference(아래 코드에서는 `-`)를 하는 데에 O(n).
- set에 pop을 하는 데에 O(1).
- 총 O(n).
"""


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return (set(range(len(nums) + 1)) - set(nums)).pop()
