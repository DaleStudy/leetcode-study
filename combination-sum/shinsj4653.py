"""
[문제풀이]
# Inputs
서로 다른 정수 배열 candidates
타겟 정수 target
# Outputs
서로 다른 숫자 조합들(리스트) 담은 리스트
# Constraints
unique combinations 개수: 150 이하
1 <= candidates.length <= 30
2 <= candidates[i] <= 40
All elements of candidates are distinct.
1 <= target <= 40

# Ideas
같은 숫자가 여러번 선택될 수 있음
[2,3,6,7] -> target = 7
몇 개의 숫자로 구성되는지를 기준으로?
최소 숫자 : 2, target max : 40 -> 한 조합 당 최대 20개 숫자

한 개로 구성:
7

두 개
5 2
4 3

세 개
2 2 3


2 3 5 -> 8

8 0
7 1
6 2
5 3
4 4

1. 한 개인 경우랑 두 개인 경우만 카운트
재귀 돌면서 후보에 있다면 그 후보 담은 리스트 반환
점점 올라가면서 return 된 리스트들 더해서 반환

근데 구현 방법이 쉽게 떠오르지 않음..

결국 어찌저찌 최종 리스트들이 반환되게끔 구현하긴 했지만, dp의 장점도 못살리고, set으로 tuple중복 없애려는 구현방법도 실패..

정답 참고

[회고]

다시 풀면서 막힌 포인트

1. 재귀
→ dfs(i, total + num)

나는 dfs(start, sum(nums)) 로 해버렸다

- sum 대신 total + num 으로 지금까지의 합을 갱신하면 더 효율적!
- start를 넣으면 중복 가짓수 발생.. i를 넣어야 중복 없이 카운트 가능

⇒ 재귀 풀 때 어떤 값을 인자값으로 넣어야 하는지를 설정하는게 가장 어려운듯..연습 많이 해야할듯..


2. DP
다시 풀면서 막힌 포인트

→ dp[num].append(combination + [candidate])

나는 dp[num].append(combination + [num]) 을 해버렸다

따라서, 후보군들로 이뤄진 후보가 아니라,

누적된 합이 적용된 리스트들이 후보로 인식되어 최종 반환 리스트에 들어가졌다.
어떤 변수를 어디에 넣어야 할지, 구현 로직(흐름)을 다시 정리! 복습!
"""

# 1번째 코드
# from collections import defaultdict
#
#
# class Solution:
#     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
#         ret = []
#
#         if target == 1:
#             return ret
#
#         elif target == 2:
#             if target in candidates:
#                 ret.append([target])
#             return ret
#
#         dp = defaultdict(set)
#
#         for num in candidates:
#             if num == target:
#                 ret.append([num])
#
#         candidates = set(candidates)
#
#         def dfs(num):
#             if num < 2:
#                 return
#
#             if num < 4:
#                 if num in candidates:
#                     return [num]
#
#             else:
#                 for i in range(2, num // 2 + 1):
#                     # dp[num].add(dfs(target - num) + dfs(num))
#                     return dfs(num - i) + dfs(i)
#
#         for num in range(2, target // 2 + 1):
#             print(dfs(target - num) + dfs(num))
#             dp[num].add(tuple(dfs(target - num) + dfs(num)))
#
#         temp = set()
#         for value in dp.values():
#             print(value)
#             # temp.add(value)
#
#         for t in temp:
#             ret.append(list(t))
#
#         return ret

# 2번째 코드 : dp 활용
class Solution:
    def combinationSum(candidates, target):
        dp = [[] for _ in range(target + 1)]
        dp[0] = [[]]
        for candidate in candidates:
            for num in range(candidate, target + 1):
                for combination in dp[num - candidate]:
                    dp[num].append(combination + [candidate])
        return dp[target]

    combinationSum([2, 3, 5], 8)

# 3번째 코드 : 재귀 활용
class Solution:
    def combinationSum(candidates, target):
        output, nums = [], []

        def dfs(start, total):
            if total > target:
                return
            if total == target:
                return output.append(nums[:])
            for i in range(start, len(candidates)):
                num = candidates[i]
                nums.append(num)
                dfs(i, total + num)
                nums.pop()

        dfs(0, 0)
        return output
    combinationSum([2, 3, 5, 7], 7)


