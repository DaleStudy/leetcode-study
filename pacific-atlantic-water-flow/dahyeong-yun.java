/**
 * heights 의 행의 갯수 m, 열의 갯수를 n 이라 할 때,
 * 
 * TC : O
 *   - m * n 만큼 순회 하므로 O(m * n)
 * SC : O(m * n)
 *   - m * n 크기의 boolean 배열을 2개 사용하므로 O(m * n) 
 * 
*
 * [최악의 콜스택 깊이 O(m * n) 예시 행렬 (4x4, 총 16개 셀)]
 * 
 * 숫자가 1부터 16까지 1씩 증가하며 단 하나의 경로로만 이어지는 형태:
 * 
 *  (0,0) [ 1] -> [ 2] -> [ 3] -> [ 4]
 *                                  |
 *  (1,0) [ 8] <- [ 7] <- [ 6] <- [ 5]
 *          |
 *  (2,0) [ 9] -> [10] -> [11] -> [12]
 *                                  |
 *  (3,0) [16] <- [15] <- [14] <- [13]
 * 
 * - (0, 0)에서 Pacific DFS 시작 시:
 *   1 -> 2 -> 3 -> ... -> 15 -> 16 까지 리턴 없이 단일 경로로 쭉 재귀 호출됨.
 * - 결과: 16(m * n)개의 함수 호출 프레임이 스택에 동시에 쌓여 최대 깊이 도달.
 */
class Solution {
    int [][] heights;
    int rowLimit = 0;
    int colLimit = 0;
    int[][] directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

    public List<List<Integer>> pacificAtlantic(int[][] heights) {   
        this.heights = heights;
        this.rowLimit = heights.length;
        this.colLimit = heights[0].length;    

        boolean[][] pacific = new boolean[rowLimit][colLimit];
        boolean[][] atlantic = new boolean[rowLimit][colLimit];

        for(int row = 0; row < rowLimit; row++) {
            dfs(row, 0, heights[row][0], pacific);
            dfs(row, colLimit - 1, heights[row][colLimit - 1], atlantic);
        }

        for(int col = 0; col < colLimit; col++) {
            dfs(0, col, heights[0][col], pacific);
            dfs(rowLimit - 1, col, heights[rowLimit - 1][col], atlantic);
        }

        List<List<Integer>> answer = new ArrayList<>();
        for(int row = 0; row < rowLimit; row++) {
            for(int col = 0; col < colLimit; col++) {
                if(pacific[row][col] && atlantic[row][col]) {
                    List<Integer> comb = List.of(row, col);
                    answer.add(comb);
                }
                
            }
        }
        return answer;
    }

    public void dfs(int row, int col, int prevHeight, boolean[][] oceanFlag) {
        if(row < 0 || col < 0 || row >= rowLimit || col >= colLimit) return; 
        if(oceanFlag[row][col] || this.heights[row][col] < prevHeight) return;

        oceanFlag[row][col] = true;

        for(int[] d : directions) {
            dfs(row + d[0], col + d[1], this.heights[row][col], oceanFlag);
        }
    }
}
