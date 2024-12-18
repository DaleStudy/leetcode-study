class Solution {
    public int climbStairs(int n) {
        // dp 응용 버전
        // 시간복잡도 : O(N), 공간복잡도 : O(1)

        int prev = 1, curr = 1;

        if (n == 1) return prev;

        for (int i = 2; i < n; i++) {
            int now = curr + prev;
            prev = curr;
            curr = now;
        }

        return curr;
    }
}
