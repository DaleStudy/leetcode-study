/*
[문제풀이]
- 1 또는 2로 n을 만들 수 있는 전체 가지수 구하기
- dfs (X) 시간초과
    class Solution {

        public int climbStairs(int n) {
            return dfs(n);
        }

        private int dfs(int n) {
            if (n == 0) {
                return 1;
            }
            if (n < 0) {
                return 0;
            }
            return dfs(n - 1) + dfs(n - 2);
        }
    }

- DP (O)
time: O(N), space: O(1)

[회고]
규칙을 찾으려고 했었는데 못찾았다..
피보나치 수열.. 풀었던 문제인데.. 생각하자;
F(N) = F(n-1) + F(n-2)
*/
class Solution {

    public int climbStairs(int n) {
        if (n <= 3) {
            return n;
        }

        int prev1 = 3;
        int prev2 = 2;
        int current = 0;
        for (int i = 4; i <= n; i++) {
            current = prev1 + prev2;
            prev2 = prev1;
            prev1 = current;
        }
        return current;
    }
}
