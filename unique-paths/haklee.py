"""TC: O(m + n), SC: O(1)

아이디어:
오른쪽으로 가는 회수 m-1, 아래로 가는 회수 n-1을 섞을 수 있는 방법의 수를 구하면 된다.
즉, m+n-2회의 이동 중 m-1개를 뽑아서 오른쪽으로 가고, 나머지를 아래로 가면 된다.
즉, (m+n-2)C(m-1)을 계산하면 된다.

큰 수 연산이 가능한 언어를 사용하면 nCk = n! / (k! * (n - k)!) 값을 계산하면 된다.
파이썬의 math.comb 함수는 아래와 같이 작동한다.
(ref: https://docs.python.org/ko/3/library/math.html#math.comb)
- math.comb(n, k)을 계산하면 k <= n이면 n! / (k! * (n - k)!)로 평가되고, k > n이면 0으로 평가됩니다.
이 함수를 써서 나온 결과값을 그대로 반환하자.

SC:
- 곱셈, 나눗셈 연산 결과 값 관리. O(1).
- 아주 큰 숫자를 다룰 경우 이렇게 보면 안 될 수도 있지만, 문제 조건을 보아하니 int64 범위 내에서
  곱셈과 나눗셈 연산 값들이 모두 처리되는 것으로 보인다. 즉, SC가 그리 중요하지는 않다.

TC:
- (m+n-2)C(m-1) = (m+n-2)! / (m-1)! * (n-1)!
- 각 곱셈 값을 구하는 데에 O(m + n), O(m), O(n). 셋 다 더하면 O(m + n).
- 나눗셈에 O(1).
- 종합하면 O(m + n)
"""

from math import comb


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return comb(m + n - 2, n - 1)
