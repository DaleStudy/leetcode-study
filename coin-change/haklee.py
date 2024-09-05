"""TC: O(m*n), SC: O(n)

coin 종류: m
amount 크기: n

아이디어: 
값 k를 만들때 필요한 최소 동전의 수를 f(k)라고 하자.
f(k)는 다음의 경우 중 제일 작은 값이다.
  - 동전 c1을 마지막으로 더해서 k를 만들었다. f(k-c1) + 1개의 동전 필요.
  - 동전 c2을 마지막으로 더해서 k를 만들었다. f(k-c2) + 1개의 동전 필요.
  - ...
  - 동전 cm을 마지막으로 더해서 k를 만들었다. f(k-cm) + 1개의 동전 필요.
즉, f(k) = min(f(k-c1), f(k-c2), ..., f(k-cm)) + 1

이때, n보다 작은 모든 i에 대해서 한 번 f(i)값을 계산할 일이 있었으면 이를 저장해두고 사용하는 방법으로
접근해서 문제를 풀 수 있다.

SC:
- n보다 작은 모든 i에 대해 f(i)값을 저장해두는 배열 필요.
- 즉, O(n).

TC:
- 각 f(i)마다 최초 계산시 m개의 아이템을 list에 넣고 min값을 찾는 계산을 한 번 한다. O(m).
- 최초 계산이 아닐 경우 배열에 저장된 값을 가져온다. O(1).
- 각 f(i)는 f(i+c1), f(i+c2), ..., f(i+cm)을 계산할때 호출되는데, 여기에 O(m) + O(1) + ... + O(1)
  만큼의 시간이 소요되므로 종합하면 O(m) + (m+1)*O(1) = O(m) 만큼의 시간이 소요된다.
- 이러한 f(i)값이 총 n개 있다. 즉, O(m*n).
"""


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        arr = [None for _ in range(amount + 1)]  # None값은 아직 계산되지 않았다는 뜻.
        arr[0] = 0  # 초기화

        def dp(target):
            if arr[target] is None:  # 만약 아직 f(target)이 계산되지 않았다면
                # 모든 동전들 c에 대해 f(target - c)는 다음의 경우들만 유효하다.
                # - target이 동전 c의 크기 이상은 되어야 한다.
                # - 앞서 계산해본 결과 총 금액 target - c를 구할 수 없는 경우는 무시.
                #    - 구할 수 없는 것으로 판명된 경우 f(x)의 값이 -1이다.
                candidates = [
                    v for c in coins if target - c >= 0 and (v := dp(target - c)) >= 0
                ]
                # candidates에 유효한 f(target - c)값이 하나도 없으면 f(target)은 -1이다.
                # 그게 아니라면 candidates에 들어있는 값 중 제일 적은 수의 동전을 필요로 하는
                # 경우에 1을 더한 값을 f(target)에 넣어둠.
                arr[target] = -1 if len(candidates) == 0 else min(candidates) + 1
            return arr[target]

        return dp(amount)
