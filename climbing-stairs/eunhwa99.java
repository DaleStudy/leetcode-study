/**
 * 문제 풀이
 */
// n=2 (1,1), (2) -> 2 가지
// n=3 (n=2, 1), (n=1, 2) -> 2 + 1 = 3가지
// n=4 (n=3, 1), (n=2, 2) -> 3 + 2 = 5가지
// n=5 (n=4, 1) , (n=3, 2)
// n=k (n=k-1, 1), (n=k-2, 2)

/**
 * 시간/공간 복잡도
 */
// 시간 복잡도: 각 칸을 한 번씩 방문 -> O(n)
// 공간 복잡도: DP 배열 크기 ->  O(n)
class Solution {
    public int climbStairs(int n) {
        int[] cntArray = new int[n + 1];
        cntArray[0] = 1;
        cntArray[1] = 1;
        for (int i = 2; i <= n; ++i) {
            cntArray[i] = cntArray[i - 1] + cntArray[i - 2];
        }
        return cntArray[n];
    }
}
