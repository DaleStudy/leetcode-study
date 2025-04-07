// NOTE: 백준 N과 M문제와 거의 동일한 문제
// memo(n) = memo(n-1)의 경우에 수에서 1칸을 올라가는 경우 + memo(n-2) 의 경우의 수에서 2 칸을 올라가는 경우의 점화식으로 표현됨.
// 시간 복잡도: O(n)
class Solution {
    public int climbStairs(int n) {
        int[] memo = new int[n + 1];


        if(n < 3) {
            return n;
        }

        memo[1] = 1;
        memo[2] = 2;
        for(int i = 3; i < memo.length; i++) {
            memo[i] = memo[i - 1] + memo[i - 2];
        }
        
        return memo[n];
    }
}
