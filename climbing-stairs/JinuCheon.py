# 재귀를 만드는 것이 잘 생각나지 않아서, 이렇게 저렇게 시도해보다 결국 LLM 도움.
# 그렇지만 제출 결과 Time Out.
# 2^N 복잡도임. max 45 의 경우 35,184,372,088,832.
class Solution:
    def climbStairs(self, n: int) -> int:
        # 1 -> 한칸만 가능
        # 2 -> (1,1) or (2)
        if n <= 2:
            return n;

        # 1칸 진행한 케이스 + 2칸 진행한 케이스
        return self.climbStairs(n-1) + self.climbStairs(n-2);

# memonization 적용. 실무를 하고나서 이걸 보니, 캐싱이라고 부르고 싶다.
# 1~N 숫자 하나당 한번의 계산을 하게 되니, 시간복잡도는 O(1) 이다.
# 이게 왜 easy 난이도지? 잊어먹었다가 주말에 자력으로 풀어보자.
class Solution:
    def climbStairs(self, n: int) -> int:
        self.memo = {}
        return self.dfs(n)

    def dfs(self, n: int) -> int:
        if n <= 2:
            return n

        # 이미 해당 수를 계산한 적이 있다면 early return.
        if n in self.memo:
            return self.memo[n]

        # 새로운 결과가 있으면 무조건 저장.
        self.memo[n] = self.dfs(n - 1) + self.dfs(n - 2)
        return self.memo[n]


# yuseok89 님 피드백 반영.
# 점화식(recursive relation): 수열의 항을 그 이전 항들을 이용해서 정의하는 식.
# 함수 호출 오버헤드 제거 & 안정성
class Solution3:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return n
        
        dp = [0] * (n+1)

        # set init values
        dp[1] = 1
        dp[2] = 2

        # i 번째 계단 오르는 경우의 수: 1칸 + 2칸 경우의 수의 합
        for i in range(3, n+1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n];
