public class Geegong {

    /**
     * 1. vectors 를 정하고 이진트리를 dfs 처럼 방향을 주어가며 훑어간다.
     * 그런데 time limit exceeded ㅠㅠ
     * => 두 방향으로 계속 뻗어가기 때문에 time complexity 가 (m+n)^2 까지 된다 흡
     *
     * 2. dp 풀이 방법, 1차원 배열로 생각했을 때 dp배열의 인덱스는 인덱스만큼의 row, column 까지 도달하는 방법의 수를 계속해서
     * 누적해가는 방법으로 진행
     *
     * @param m
     * @param n
     * @return
     */
    public static int[][] vectors = {{0,1}, {1,0}};
    public int uniquePaths(int m, int n) {
        // case 1. tle ㅠㅠ
//        return dfs( 0, 0, m, n);

        // 뭔가 m*n 만큼의 배열이어야 할 것 같지만 사실 각 row마다의 column들에 방문할때의 방문 가능 갯수를 누적해가기때문에 n 만큼만 있어도 된다.
        int[] dp = new int[n];

        dp[0] = 1; // 시작점부터 path 가능 갯수 1
        for(int rowIdx = 0; rowIdx < m; rowIdx++) {
            // 1부터 세는 이유는... 어차피 오른쪽으로 움직이기 때문예?
            for(int colIdx = 1; colIdx < n; colIdx++) {
                // dp[colIdx - 1] : 직전 column기준 0에서부터 도달할 수 있는 방법의 수
                // dp[colIdx] : rowIdx - 1이 었을때 0에서부터 [rowIdx - 1][colIdx] 까지 도달할 수 있는 방법의 수
                dp[colIdx] = dp[colIdx - 1] + dp[colIdx];
            }
        }

        return dp[n - 1];
    }

//    public int dfs(int startRow, int startBottom, int m, int n) {
//        if (startRow == m - 1 && startBottom == n - 1) {
//            return 1;
//        } else if (startRow >= m || startBottom >= n) {
//            return 0;
//        }
//
//        int result = 0;
//
//        for (int[] vector : vectors) {
//            result += dfs(vector[1] + startRow, vector[0] + startBottom, m, n);
//        }
//
//        return result;
//    }
}

