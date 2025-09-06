public class Geegong {

    /**
     * 1. 하나씩 훑어가면서 1이 되는 시점을 찾아 그 시점부터 dfs 로 방향값을 주어
     * 방문한 곳은 0으로 바꿔버려 다시는 탐색하지 못하도록 막아버림
     * 모든 방향값을 주면서 0으로 메꾼 후 1을 리턴하고 리턴된 값들을 누적하면 만들어낼 수 있는 섬의 총 갯수가 된다
     * time complexity : O (m*n*4) => O(m*n)
     * space complexity : O(m*n) // 따로 memoization 을 위한 변수는 없으나 재귀로 인해 콜스택 발생
     */
    public static int[][] vectors = {{0,1}, {1,0}, {0,-1}, {-1,0}};
    public int numIslands(char[][] grid) {

        int totalNumberOfIslands = 0;

        for (int rowIdx=0; rowIdx < grid.length; rowIdx++) {
            for (int colIdx=0; colIdx < grid[0].length; colIdx++) {
                // 1이 되는 시점부터 섬이 되는지 체크한다.
                if (grid[rowIdx][colIdx] == '1') {
                    totalNumberOfIslands += dfs(grid, rowIdx, colIdx);
                }
            }
        }
        return totalNumberOfIslands;
    }

    public int dfs(char[][] origin, int rowIdx, int colIdx) {
        if (rowIdx < 0 || colIdx < 0) {
            // 의미 없는 리턴. 단순히 콜스택 이전으로 돌아가기 위해 임의값 리턴
            return 1;
        }

        if (rowIdx >= origin.length || colIdx >= origin[0].length) {
            // 의미 없는 리턴. 단순히 콜스택 이전으로 돌아가기 위해 임의값 리턴
            return 1;
        }

        if (origin[rowIdx][colIdx] == '0') {
            // 의미 없는 리턴. 단순히 콜스택 이전으로 돌아가기 위해 임의값 리턴
            return 1;
        }

        origin[rowIdx][colIdx] = '0'; // 0 으로 셋팅해서 다음 섬을 찾을때 방문하지 못하도록 방어한다.

        for (int[] vector : vectors) {
            int moveRow = vector[0];
            int moveCol = vector[1];

            dfs(origin, rowIdx + moveRow, colIdx + moveCol);
        }

        // 섬이 되는 구역을 다 돌았다면 하나의 섬이 하나 된다고 판단이 되므로 1 리턴
        return 1;
    }

}

