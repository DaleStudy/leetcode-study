/**
 * [Problem]: [417] Pacific Atlantic Water Flow
 * (https://leetcode.com/problems/pacific-atlantic-water-flow/description/)
 */
function pacificAtlantic(heights: number[][]): number[][] {
    //시간복잡도 O(n)
    //공간복잡도 O(n)
    const result: number[][] = [];
    const rows = heights.length;
    const cols = heights[0].length;

    const pacificArea: boolean[][] = Array.from({ length: rows }, () => Array(cols).fill(false));
    const atlanticArea: boolean[][] = Array.from({ length: rows }, () => Array(cols).fill(false));

    function dfs(visited: boolean[][], row: number, col: number) {
        if (row < 0 || col < 0 || row >= rows || col >= cols) return;
        if (visited[row][col]) return;

        visited[row][col] = true;

        [
            [row - 1, col],
            [row + 1, col],
            [row, col - 1],
            [row, col + 1],
        ].forEach(([r, c]) => {
            if (r >= 0 && c >= 0 && r < rows && c < cols) {
                if (heights[r][c] >= heights[row][col]) {
                    dfs(visited, r, c);
                }
            }
        });
    }

    for (let i = 0; i < rows; i++) {
        dfs(pacificArea, i, 0);
        dfs(atlanticArea, i, cols - 1);
    }
    for (let j = 0; j < cols; j++) {
        dfs(pacificArea, 0, j);
        dfs(atlanticArea, rows - 1, j);
    }

    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < cols; j++) {
            if (pacificArea[i][j] && atlanticArea[i][j]) {
                result.push([i, j]);
            }
        }
    }

    return result;
}
