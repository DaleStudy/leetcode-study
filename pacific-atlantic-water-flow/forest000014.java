/*
# Time Complexity: O(m * n * log(m * n))
# Space Complexity: O(m * n)
  - visited, pq
DFS와 PQ를 조합하여 풀었습니다.
*/
class Solution {
    private class Cell {
        int r;
        int c;
        int h;

        Cell(int r, int c, int h) {
            this.r = r;
            this.c = c;
            this.h = h;
        }
    }

    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        int m = heights.length;
        int n = heights[0].length;
        PriorityQueue<Cell> pq1 = new PriorityQueue<>(new Comparator<Cell>() {
            @Override
            public int compare(Cell c1, Cell c2) {
                return c1.h - c2.h;
            }
        });
        PriorityQueue<Cell> pq2 = new PriorityQueue<>(new Comparator<Cell>() {
            @Override
            public int compare(Cell c1, Cell c2) {
                return c1.h - c2.h;
            }
        });
        int[][] visited = new int[m][n];

        for (int i = 0; i < m; i++) {
            pq1.offer(new Cell(i, 0, heights[i][0]));
            pq2.offer(new Cell(i, n - 1, heights[i][n - 1]));
            visited[i][0] |= 1;
            visited[i][n - 1] |= 2;
        }
        for (int i = 1; i < n; i++) {
            pq1.offer(new Cell(0, i, heights[0][i]));
            pq2.offer(new Cell(m - 1, i - 1, heights[m - 1][i - 1]));
            visited[0][i] |= 1;
            visited[m - 1][i - 1] |= 2;
        }

        int[] dr = {-1, 0, 1, 0};
        int[] dc = {0, 1, 0, -1};
        while (!pq1.isEmpty()) {
            Cell curr = pq1.poll();
            for (int i = 0; i < 4; i++) {
                int nr = curr.r + dr[i];
                int nc = curr.c + dc[i];
                if (nr < 0 || nr >= m || nc < 0 || nc >= n || heights[nr][nc] < heights[curr.r][curr.c] || (visited[nr][nc] & 1) == 1) continue;
                pq1.offer(new Cell(nr, nc, heights[nr][nc]));
                visited[nr][nc] |= 1;
            }
        }
        while (!pq2.isEmpty()) {
            Cell curr = pq2.poll();
            for (int i = 0; i < 4; i++) {
                int nr = curr.r + dr[i];
                int nc = curr.c + dc[i];
                if (nr < 0 || nr >= m || nc < 0 || nc >= n || heights[nr][nc] < heights[curr.r][curr.c] || (visited[nr][nc] & 2) == 2) continue;
                pq2.offer(new Cell(nr, nc, heights[nr][nc]));
                visited[nr][nc] |= 2;
            }
        }

        List<List<Integer>> ans = new ArrayList<>();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (visited[i][j] == 3) {
                    ans.add(new ArrayList<>(List.of(i, j)));
                }
            }
        }

        return ans;
    }
}
