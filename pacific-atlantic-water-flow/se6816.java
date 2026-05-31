/**
    BFS를 통해, 방문 지점이 겹치는 부분을 찾는 방식
 */
class Solution {
    public static int[] moveX = {0, 1, 0, -1};
    public static int[] moveY = {1, 0, -1, 0};
    public boolean[][] POvisited;
    public boolean[][] AOvisited;
    public int N;
    public int M;
    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        List<List<Integer>> result = new ArrayList<>();
        N = heights.length;
        M = heights[0].length;
        POvisited = new boolean[N][M];
        AOvisited = new boolean[N][M];
        Queue<int[]> que = new LinkedList<>();
        Queue<int[]> que2 = new LinkedList<>();

        for(int i = 0; i < M; i++) {
            POvisited[0][i] = true;
            que.add(new int[]{0, i});
            AOvisited[N-1][i] = true;
            que2.add(new int[]{N-1, i});
        }

        for(int i = 0; i < N; i++) {
            POvisited[i][0] = true;
            que.add(new int[]{i, 0});
            AOvisited[i][M-1] = true;
            que2.add(new int[]{i, M-1});
        }
        bfs(que, POvisited, heights);
        bfs(que2, AOvisited, heights);

        for(int i = 0; i < N; i++) {
            for(int j = 0; j < M; j++) {
                if(POvisited[i][j] && AOvisited[i][j]) {
                    result.add(new ArrayList<>(List.of(i, j)));
                }
            }
        }

        return result;
    }

    public void bfs(Queue<int[]> que, boolean[][] visited, int[][] heights) {
        while(!que.isEmpty()) {
            int[] node = que.poll();
            for(int i = 0; i < 4; i++) {
                int tempX = node[0] + moveX[i];
                int tempY = node[1] + moveY[i];
                if(isOutOfIndex(tempX, tempY)) {
                    continue;
                }

                if(visited[tempX][tempY]) {
                    continue;
                }
                if(heights[tempX][tempY] < heights[node[0]][node[1]]) {
                    continue;
                }

                visited[tempX][tempY] = true;
                que.add(new int[]{tempX, tempY});
            }
        }
    }

    public boolean isOutOfIndex(int x, int y){
        return x < 0 || x >= N || y < 0 || y >= M;
    }
}
