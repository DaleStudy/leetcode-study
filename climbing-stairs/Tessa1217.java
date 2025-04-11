/**
 당신은 계단을 오르고 있다. 정상에 오르기까지 n 계단을 올라야 한다.
 계단을 오를 때마다 1 계단 또는 2 계단씩 오를 수 있을 때 정상에 도달하기까지의 경우의 수를 구하시오.
 */

public class Solution {

    // 시간복잡도: O(n)
    public int climbStairs(int n) {

        if (n == 1 || n == 2) {
            return n;
        }

        int[] cases = new int[n + 1];
        cases[1] = 1;
        cases[2] = 2;
        for (int i = 3; i <= n; i++) {
            cases[i] = cases[i - 1] + cases[i - 2];
        }

        return cases[n];
    }

}

