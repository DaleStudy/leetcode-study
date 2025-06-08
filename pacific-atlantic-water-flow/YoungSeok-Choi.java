import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

// TC -> O(nm^2) 일 것으로 예상.. 
class Solution {

    public boolean[][] visit;
    public List<List<Integer>> res = new ArrayList<>();
    public int w;
    public int h;

    public int[] dx = { 0, 1, 0, -1 };
    public int[] dy = { 1, 0, -1, 0 };

    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        w = heights.length;
        h = heights[0].length;

        if (w == h && w == 1) {
            res.add(Arrays.asList(0, 0));
            return res;
        }

        for (int i = 0; i < w; i++) {
            for (int j = 0; j < h; j++) {

                boolean isTrue = false;
                visit = new boolean[w][h];

                isTrue |= dfsP(i, j, heights[i][j], heights);

                visit = new boolean[w][h];

                isTrue &= dfsA(i, j, heights[i][j], heights);

                if (isTrue) {
                    res.add(Arrays.asList(i, j));
                }
            }
        }

        return res;
    }

    public boolean dfsP(int x, int y, int prev, int[][] map) {
        if (x < 0 || y < 0) {
            return true;
        }

        if (x >= w || y >= h) {
            return false;
        }

        if (visit[x][y]) {
            return false;
        }

        if (prev < map[x][y]) {
            return false;
        }

        visit[x][y] = true;

        boolean isTrue = false;
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            isTrue |= dfsP(nx, ny, map[x][y], map);
            if (isTrue) {
                return true;
            }
        }

        return isTrue;
    }

    public boolean dfsA(int x, int y, int prev, int[][] map) {
        if (x < 0 || y < 0) {
            return false;
        }

        if (x >= w || y >= h) {
            return true;
        }

        if (visit[x][y]) {
            return false;
        }

        if (prev < map[x][y]) {
            return false;
        }

        visit[x][y] = true;

        boolean isTrue = false;
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            isTrue |= dfsA(nx, ny, map[x][y], map);

            if (isTrue) {
                return true;
            }

        }

        return isTrue;
    }
}
