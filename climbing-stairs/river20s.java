/*
 * 풀이: n번째 계단에 도달하는 경우는 다음 두 가지로 나뉜다.
 * 1. (n-1)번째 계단에서 한 계단 오르는 경우
 * 2. (n-2)번째 계단에서 두 계단 오르는 경우
 * 따라서, n개의 계단을 올라가는 방법의 경우의 수 F(n)은
 * F(n-1)과 F(n-2)의 합과 같다.
 * 시간 복잡도: O(n)
 * 공간 복잡도: O(1)
 */
class Solution {
    public int climbStairs(int n) {
        if(n == 1) return 1;

        int step1 = 1;
        int step2 = 2;

        for (int i = 3; i <= n; i++) {
            int temp = step1 + step2;
            step1 = step2;
            step2 = temp;
        }

        return step2;
    }
}
 
