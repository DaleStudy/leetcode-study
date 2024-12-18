// n=2 (1,1), (2) -> 2 가지
// n=3 (n=2, 1), (n=1, 2) -> 2 + 1 = 3가지
// n=4 (n=3, 1), (n=2, 2) -> 3 + 2 = 5가지
// n=5 (n=4, 1) , (n=3, 2)
// n=k (n=k-1, 1), (n=k-2, 2)

class Solution {
    public int climbStairs(int n) {
        int[] cntArray = new int[n + 1];
        cntArray[0] = 1;
        cntArray[1] = 1;
        for (int i = 2; i <= n; ++i) { // 시간 복잡도: O(n)
            cntArray[i] = cntArray[i - 1] + cntArray[i - 2];
        }
        return cntArray[n];
    }
}
