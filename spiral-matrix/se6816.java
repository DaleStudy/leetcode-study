/**
	구현을 통해 배열을 읽어들이는 방식
	시간 복잡도 : O(N*M)
	공간 복잡도 : O(N*M)
*/
class Solution {
    int[] moveY = {1, 0, -1, 0};
    int[] moveX = {0, -1, 0, 1};
    int N;
    int M;
    public List<Integer> spiralOrder(int[][] matrix) {
        N = matrix.length;
        M = matrix[0].length;
        boolean[][] visited = new boolean[N][M];
        List<Integer> result = new ArrayList<>();
        int curX = 0;
        int curY = 0;
        int direction = 0;
        int count = 0;
        visited[curX][curY] = true;
        result.add(matrix[curX][curY]);

        while(true) {
            if(count == 4) {
                break;
            }
            int tempX = curX + moveX[direction];
            int tempY = curY + moveY[direction];
            if(outOfIndex(tempX, tempY)) {
                direction = (direction + 1) % 4;
                count++;
                continue;
            }

            if(visited[tempX][tempY]) {
               direction = (direction + 1) % 4;
               count++;
               continue; 
            }

            curX = tempX;
            curY = tempY;
            result.add(matrix[curX][curY]);
            visited[curX][curY] = true;

            count = 0;
        }

        return result;
    }
    
    public boolean outOfIndex(int x, int y) {
        return x < 0 || x >= N || y < 0 || y >= M;
    }
}
