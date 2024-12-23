/*
i번째 칸에 가는 방법은 (1) i-2번째 칸에서 2칸을 점프하거나 (2) i-1번째 칸에서 1칸을 점프하는 2가지 방법 뿐입니다. (MECE함)
따라서, (i번째 칸에 가는 경우의 수) = (i-2번째 칸에 가는 경우의 수) + (i-1번째 칸에 가는 경우의 수)

Runtime: 0 ms (Beats: 100.00%)
Time Complexity: O(n)

Memory: 40.47 MB (Beats: 36.79%)
Space Complexity: O(1)
*/

class Solution {
    public int climbStairs(int n) {
        if (n == 1) {
            return 1;
        } else if (n == 2) {
            return 2;
        } else {
            int prev2 = 1;
            int prev1 = 2;
            int cur = 0;
            for (int i = 3; i <= n; i++) {
                cur = prev2 + prev1;
                prev2 = prev1;
                prev1 = cur;
            }
            return cur;
        }
    }
}
