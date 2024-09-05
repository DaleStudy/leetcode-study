"""TC: O(m^n), SC: O(m^n)

candidates에 있는 값의 개수: m
target의 크기: n

아이디어: 
candidates(이하 cands)에 있는 숫자들을 더해서 k를 만드는 방법을 f(k)라고 하자.
f(k)는 다음의 경우들을 종합한 것이다.
  - cands에 있는 c1을 마지막으로 더해서 k를 만들었다. 즉, f(k-c1)에 있는 모든 방법의 끝에 c1을 더함.
  - cands에 있는 c2를 마지막으로 더해서 k를 만들었다. 즉, f(k-c2)에 있는 모든 방법의 끝에 c2을 더함.
  ...
  - cands에 있는 cm을 마지막으로 더해서 k를 만들었다. 즉, f(k-cm)에 있는 모든 방법의 끝에 cm을 더함.

이렇게 하면 문제는, 하나의 값을 만드는 데에 중복된 경우가 나올 수 있다는 것이다.
e.g.) candidates = [2, 3], target = 5
f(2) = [[2]]
f(3) = [[3]]
위의 값을 활용해서 f(5)를 구하면
f(5) = [f(2)의 방법들의 끝에 3을 붙임] + [f(3)의 방법들의 끝에 2를 붙임]
     = [[2, 3]] + [[3, 2]]
     = [[2, 3], [3, 2]]

그래서 마지막에 같은 아이템으로 이루어진 리스트를 찾아서 중복을 제거해준다.

이번 문제에서는 [2, 2, 3], [2, 3, 2], [3, 2, 2] 같이 들어가는 아이템의 순서만 다른 경우를 같은 것으로
보았기 때문에 마지막에 중복을 제거했지만, 만약 이들을 서로 다른 방법으로 보는 문제가 주어진다면 위의
결과를 그대로 리턴하면 된다.


SC:
- 문제 특성상 f(i)에 들어갈 수 있는 방법의 수는
    - i를 만드는 방법의 길이는 O(i).
        - cands에 1이 있고 이 1로 가득 채운 방법 [1, 1, ..., 1]을 생각하면 편하다.
        - cands의 최소값이 어떤 상수 x라고 해도 [x, x, ..., x]에는 i/x가 들어가는데, O(i/x)는 O(i).
    - 각 방법에 들어있는 아이템은 m가지 경우의 수가 가능. [(c1, c2, ..., cm 중 하나), ..., (c1, c2, ..., cm 중 하나)]
    - 즉, f(i)에는 O(m^i)가지 경우가 들어갈 수 있다.
- f(1), f(2), ..., f(n)을 다 더하면 O(m^1) + O(m^2) + ... + O(m^n) = O(m^n)이 된다.
- 즉, O(m^n).

TC:
- 위의 SC와 같은 방식으로 접근이 가능하다. O(m^n).
"""


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [[] for _ in range(target + 1)]  # 초기화.
        dp[0] = [[]]  # 0을 만드는 방법은 아무 숫자도 넣지 않는 것 한 가지 방법이 있다.
        for cur in range(1, target + 1):  # f(i)를 1부터 계산해나가면서 채우기 시작.
            for cand in candidates:
                prev = cur - cand
                if prev >= 0:
                    dp[cur] += [combi + [cand] for combi in dp[prev]]

        # 마지막에 중복된 경우를 제거해준다.
        return list(set([tuple(sorted(i)) for i in dp[target]]))


"""
아이디어:
중간중간 계산하면서 중복된 값을 제거하면서 f(i)값을 관리하는 식으로 커팅하는 것이 가능하다.
각 방법은 [c1, ...c1, c2, ..., c2, ... , cm, ..., m] 꼴이 되는데,
          [         ^            ^ ... ^           ] 
각 f(i)마다 위의 `^` 표시를 해둔 곳을 찾는 방법의 수만큼 공간이 필요하다.
이 숫자는 대략 (i choose m-1)이라고 생각할 수 있다.

그러므로 SC와 TC 모두 O(n choose m) = O((n/m)^m)...?
(ref: https://en.wikipedia.org/wiki/Binomial_coefficient#Bounds_and_asymptotic_formulas)
"""


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [[] for _ in range(target + 1)]
        dp[0] = [[]]
        for cur in range(1, target + 1):
            for cand in candidates:
                prev = cur - cand
                if prev >= 0:
                    dp[cur] += [combi + [cand] for combi in dp[prev]]
            dp[cur] = list(set([tuple(sorted(i)) for i in dp[cur]]))
        return list(set([tuple(sorted(i)) for i in dp[target]]))


"""
아이디어:
만들고 나서 중복된 경우를 제거하지 말고, 처음부터 중복된 결과를 만들지 않는 것도 방법이다.
각 방법마다 해당 방법에서 사용한 최대 candidate 인덱스를 달아두고, 이후 해를 구할 때는 해당
인덱스 이상의 candidate만 추가할 수 있도록 단서를 달아두는 방식으로 구현 가능하다.
e.g.) candidate = [2, 5, 3]
f(10)에 들어있을 수 있는 방법은
- ([2, 2, 2, 2, 2], 0) : 마지막 아이템 이후에 2, 5, 3 전부 등장 가능.
- ([5, 5], 1) : 마지막 아이템 이후에 5, 3만 등장 가능.
- ([2, 5, 3], 2) : 마지막 아이템 이후에 3만 등장 가능.
- ([2, 2, 3, 3], 2) : 마지막 아이템 이후에 3만 등장 가능.

SC와 TC는 바로 위에서 O(n choose m)을 계산한 것과 같을 것으로 보인다.
"""


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [[] for _ in range(target + 1)]
        dp[0] = [([], 0)]  # (방법, 사용 가능한 candidate index 최소값) 쌍.
        for cur in range(1, target + 1):
            for i in range(len(candidates)):
                prev = cur - candidates[i]
                if prev >= 0:
                    dp[cur] += [
                        (combi[0] + [candidates[i]], i)
                        for combi in dp[prev]
                        if i >= combi[1]
                    ]
        return [i[0] for i in dp[target]]  # 방법만 추출해서 리턴한다.
