"""TC: O(n), SC: O(n)

아이디어: 
다음의 세 상황 중 하나가 될 것이다.
- 0이 둘 이상 포함. 모든 결과값이 0이 된다.
- 0이 하나 포함.
    - 0에 해당하는 인덱스에는 nums에 있는 숫자들 중 0 말고 나머지 숫자들을 전부 곱한 값.
    - 그 외 모두 0.
- 0이 하나도 없다.
    - nums에 있는 모든 숫자들을 곱한 값을 p라고 할때, 각 인덱스 i마다 p를 nums[i]로 나눈 값.

그러므로, 먼저 nums에 있는 숫자들을 돌면서
- 0이 아닌 숫자를 전부 곱한 값 p를 만든다.
- 0이 들어있는 인덱스를 찾는다.

그 다음
- 0이 들어있는 인덱스의 길이를 보고 위의 세 상황 중 하나에 대응해서 결과값을 리턴한다.

SC:
- 0이 아닌 숫자들을 곱한 값 p를 관리할때 O(1)
- 0이 등장하는 인덱스 zero_ind를 관리할때 O(n)
- 결과로 리턴할 값 O(n)
- 종합하면 O(n).

TC:
- nums값을 한 번 순회하면서 p, zero_ind값을 업데이트 할때 O(n)
- 결과로 리턴할 값 만들때 O(n)
- 종합하면 O(n).
"""


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_ind = []
        p = 1
        for i, e in enumerate(nums):
            if e == 0:
                zero_ind.append(i)
            else:
                p *= e

        sol = [0] * len(nums)
        if len(zero_ind) > 1:
            return sol
        elif len(zero_ind) == 1:
            sol[zero_ind[0]] = p
            return sol
        else:
            return [p // i for i in nums]
