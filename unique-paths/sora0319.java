class Solution {
    public int uniquePaths(int m, int n) {
        int[][] pathN = new int[m][n];
        boolean[][] visited = new boolean[m][n];
        pathN[0][0] = 1;

        bfs(pathN, visited);
        return pathN[m-1][n-1];
    }
    public void bfs(int[][] pathN, boolean[][] visited){
        Queue<Pair> paths = new LinkedList<>();
        int[] mx = {0, 1};
        int[] my = {1, 0};

        paths.offer(new Pair(0,0));

        while(!paths.isEmpty()){
            Pair p = paths.poll();

            for(int i = 0; i < 2; i++){
                int nx = mx[i] + p.x;
                int ny = my[i] + p.y;

                if(nx >= pathN.length || ny >= pathN[0].length) continue;
                pathN[nx][ny] += pathN[p.x][p.y];
                if(!visited[nx][ny]){
                    paths.offer(new Pair(nx, ny));
                    visited[nx][ny] = true;
                }

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

