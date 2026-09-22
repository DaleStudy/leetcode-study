import java.util.ArrayDeque;
import java.util.Deque;

class Solution {
    private static final int[][] DIRECTIONS = {
            {0, 1},
            {0, -1},
            {1, 0},
            {-1, 0}
    };

    private static final char WATER = '0';
    private static final char LAND = '1';

    private record Position(int row, int column) {
    }

    /**
     * 격자를 순회하며 아직 방문하지 않은 육지를 발견할 때마다
     * 연결된 하나의 섬을 반복형 DFS로 모두 방문 처리한다.
     *
     * 시간 복잡도: O(m * n)
     * 공간 복잡도: O(m * n)
     */
    public int numIslands(char[][] grid) {
        int islandCount = 0;

        for (int row = 0; row < grid.length; row++) {
            for (int column = 0; column < grid[row].length; column++) {
                if (grid[row][column] != LAND) {
                    continue;
                }

                // 아직 방문하지 않은 육지는 새로운 섬의 시작점이다.
                islandCount++;
                markIslandAsVisited(grid, row, column);
            }
        }

        return islandCount;
    }

    /**
     * 시작 위치와 상하좌우로 연결된 모든 육지를 방문 처리한다.
     * 재귀 호출로 인한 스택 오버플로를 피하기 위해 별도의 스택을 사용한다.
     */
    private static void markIslandAsVisited(
            char[][] grid,
            int startRow,
            int startColumn
    ) {
        Deque<Position> stack = new ArrayDeque<>();
        stack.push(new Position(startRow, startColumn));

        // 스택에 넣는 시점에 방문 처리하여 같은 위치가 중복으로 들어가는 것을 방지한다.
        grid[startRow][startColumn] = WATER;

        while (!stack.isEmpty()) {
            Position current = stack.pop();

            for (int[] direction : DIRECTIONS) {
                int nextRow = current.row() + direction[0];
                int nextColumn = current.column() + direction[1];

                if (!isInBounds(grid, nextRow, nextColumn)) {
                    continue;
                }

                if (grid[nextRow][nextColumn] != LAND) {
                    continue;
                }

                grid[nextRow][nextColumn] = WATER;
                stack.push(new Position(nextRow, nextColumn));
            }
        }
    }

    private static boolean isInBounds(
            char[][] grid,
            int row,
            int column
    ) {
        return row >= 0
                && row < grid.length
                && column >= 0
                && column < grid[0].length;
    }
}
