# 7기 풀이
# 시간복잡도: O(n)
#  - memoization을 하기 때문에 각 인덱스 별로 가능한 수를 계산할 때 한 번 씩만 계산
# 공간복잡도: O(n)
#  - 문자열의 길이만큼 memo 값이 늘어남
class Solution:
    # DP를 이용해 문제를 풀면 된다.
    # 각 인덱스로 별로 문자열을 잘랐을 때의 가능한 디코딩 방법 수를 memo한다
    def numDecodings(self, s: str) -> int:
        len_s = len(s)
        memo = {}

        def dfs(index):
            if index == len_s:  # 끝까지 탐색했다면 가능한 디코딩 방법이므로 1을 return
                return 1

            if s[index] == '0':  # 현재 index의 문자가 '0'이면 해당 방법은 디코딩이 불가한 것으로 판단 0을 return
                return 0
            
            if index in memo:  # 이미 저장되어 있다면 memo 값을 return
                return memo[index]

            result = dfs(index + 1)  # index로부터 한 자리 수만 계산할 때, 다음 계산은 index + 1이 된다

            if (
                index + 1 < len_s
                and int(s[index:index + 2]) <= 26
            ):  # index~index+1의 문자열이 26보다 작은 두 자리 수일 때만 index + 2번째 계산을 한다
                result += dfs(index + 2)

            memo[index] = result  # memoization을 한다
            return result

        return dfs(0)
