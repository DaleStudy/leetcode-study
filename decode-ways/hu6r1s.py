class Solution:
    def numDecodings(self, s: str) -> int:
        """
        1. 재귀 알고리즘 사용
        _
        226 -> B, 26
        _
        26 -> B, 6
        _
        6 -> F "BBF"
        __
        26 -> Z "BZ"
        __
        226 -> V, 6
        _
        6 -> F "VF"

        시간복잡도: O(2^n) - 중복 계산이 많아 매우 비효율적
        공간복잡도: O(n) - 최대 재귀 깊이만큼 스택 사용
        """
        # def dfs(start):
        #     if start == len(s):
        #         return 1
        #     if s[start] == "0":
        #         return 0
        #     if start + 1 < len(s) and int(s[start:start+2]) < 27:
        #         return dfs(start+1) + dfs(start+2)
        #     else:
        #         return dfs(start+1)
        # return dfs(0)
        
        """
        2. 재귀 + 메모리제이션
        시간복잡도: O(n) - 각 시작 위치에 대해 한 번만 계산
        공간복잡도: O(n) - 메모이제이션 딕셔너리와 재귀 스택
        """
        # memo = {len(s): 1}
        # def dfs(start):
        #     if start in memo:
        #         return memo[start]
        #     if s[start] == "0":
        #         memo[start] = 0
        #     elif start + 1 < len(s) and int(s[start:start+2]) < 27:
        #         memo[start] = dfs(start+1) + dfs(start+2)
        #     else:
        #         memo[start] = dfs(start+1)

        #     return memo[start]
        # return dfs(0)
        
        """
        3. DP
        시간복잡도 (Time Complexity): O(n)
        - 문자열 s의 길이만큼 한 번의 루프를 도는 DP 방식

        공간복잡도 (Space Complexity): O(n)
        - 길이 n+1짜리 dp 배열 사용
        - 공간 최적화를 하면 O(1)로 줄일 수 있음
        """
        dp = [0] * len(s) + [1]
        for i in range(len(s)-1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            elif i + 1 < len(s) and int(s[i:i+2]) < 27:
                dp[i] = dp[i+1] + dp[i+2]
            else:
                dp[i] = dp[i+1]
        return dp[0]
