// 풀이 핵심
// dp나 1차원 배열 2개를 이용하는 방식의 핵심은 결국 현재 값은 왼쪽 값과 상단 값이 더해진 값으로 이루어진다는 것이다.
// dp는 2차원 배열 공간 모두를 사용해야하지만, 1차원 배열 2개의 경우 2n의 공간을 이용해 현재 값을 만들어 나가게 된다.
class Solution {
    public int uniquePaths(int m, int n) {
        // (1) dp - 2차원 배열 이용
        // 시간복잡도 : O(m * n), 공간복잡도 : O(m * n)
        int[][] dp = new int[m][n];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (i == 0 && j == 0) {
                    dp[i][j] = 1;
                    continue;
                }

                int pathsFromLeft = (j - 1 >= 0) ? dp[i][j - 1] : 0;
                int pathsFromUp = (i - 1 >= 0) ? dp[i - 1][j] : 0;
                dp[i][j] = pathsFromLeft + pathsFromUp;
            }
        }

        return dp[m - 1][n - 1];

        // (2) 1차원 배열 2개 이용
        // 시간복잡도 : O(m * n), 공간복잡도 : O(n)
        int[] aboveRow = new int[n];
        Arrays.fill(aboveRow, 1);

        for (int row = 1; row < m; row++) {
            int[] currentRow = new int[n];
            Arrays.fill(currentRow, 1);
            for (int col = 1; col < n; col++) {
                currentRow[col] = currentRow[col - 1] + aboveRow[col];
            }
            aboveRow = currentRow;
        }

        return aboveRow[n - 1];
    }
}
