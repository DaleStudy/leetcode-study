"""TC: O(n), SC: O(n)

아이디어:
- nums 안에는 여러 consecutive sequence(이하 cs)가 존재할 것이다(길이 1인 것까지 포함).
- 이 cs는 모두 제일 앞 숫자를 가지고 있다.
- 제일 앞 숫자는 그 숫자 바로 앞에 숫자가 없다는 특징을 가지고 있다.
    - 즉, i가 제일 앞 숫자라면 i-1은 nums 안에 없다.
- nums에서 제일 앞 숫자를 찾은 다음, 이 숫자부터 뒤로 이어지는 cs를 찾아서 길이를 구할 수 있다.
- cs의 길이 중 제일 긴 것을 찾아서 리턴하면 된다.

SC:
- set(nums)에서 O(n).
- 위 set에서 모든 아이템을 돌면서 i-1이 set 안에 포함되지 않는 i를 찾아서 리스트로 만들때 O(n).
- 총 O(n).

TC:
- set(nums)에서 O(n).
- 위 set에서 모든 아이템을 돌면서 i-1이 set 안에 포함되지 않는 i를 찾는 데에 O(n).
- 각 cs의 제일 앞 숫자부터 이어지는 숫자들이 set 안에 있는지 체크하는 데에 총 O(n).
- 총 O(n).
"""


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)  # TC:O(n), SC:O(n)
        seq_start_candidate = [i for i in s if i - 1 not in s]  # TC:O(n), SC:O(n)
        sol = 0

        # 아래의 for문 내에서는 s에 속한 아이템에 한 번씩 접근한다. TC:O(n)
        for i in seq_start_candidate:
            seq_len = 1
            while i + seq_len in s:
                seq_len += 1
            sol = max(seq_len, sol)
        return sol
