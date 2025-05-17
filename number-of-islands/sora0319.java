class Solution {
    public int numIslands(char[][] grid) {
        Queue<Pair> island = new LinkedList<>();
        int N = grid.length;
        int M = grid[0].length;
        boolean[][] visited = new boolean[N][M];
        int count = 0;

        for(int i = 0; i < N; i++){
            for(int j = 0; j < M; j++){
                if(!visited[i][j] && grid[i][j] == '1'){
                    island.offer(new Pair(i, j));
                    visited[i][j] = true;
                    bfs(grid, visited, island);
                    count++;
                }
            }
        }
        return count;
    }
    public void bfs(char[][] grid, boolean[][] visited, Queue<Pair> island){
        int[] mx = {-1, 1, 0, 0};
        int[] my = {0, 0, -1, 1};


        while(!island.isEmpty()){
            Pair p = island.poll();
            for(int i = 0; i < 4; i++){
                int nx = mx[i] + p.x;
                int ny = my[i] + p.y;

                if(nx < 0 || ny < 0||  nx >= grid.length || ny >= grid[0].length) continue;
                if(visited[nx][ny] || grid[nx][ny] == '0') continue;

                island.offer(new Pair(nx, ny));
                visited[nx][ny] = true;
            }

        }
    }

    class Pair{
        int x;
        int y;
        Pair(int x, int y){
            this.x = x;
            this.y = y;
        }
    }
}

