public class Solution {
    //피보나치 수열과 동일하다.
    public int climbStairs(int n) {
        // n < 3 일 때 n번째 계단에 오르는 방법은 n개
        if (n < 3) return n;
        // n >= 3 일 때는 (n-1)번째 계단에 오르는 방법 + (n-2)번째 계단에 오르는 방법
        int sec = 0;
        int prev = 1;
        int current = 2;
        for (int i = 3; i <= n; i++) {
            //i값이 증가할수록 (i-1)번째 값과 (i-2)번째 값이 각각 현재의 값과 이전 값으로 변경된다.
            sec = prev;
            prev = current;
            //현재 값은 (i-1)번째 값과 (i-2)번째 값의 합
            current = prev + sec;
        }
        return current;
    }
}
