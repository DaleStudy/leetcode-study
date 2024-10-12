/**
 * https://leetcode.com/problems/two-sum
 * time complexity : O(m x m)
 * space complexity : O(m x n)
 */
function pacificAtlantic(heights: number[][]): number[][] {
    const m = heights.length;
    const n = heights[0].length;
    const pacific: boolean[][] = Array.from({ length: m }, () => Array(n).fill(false));
    const atlantic: boolean[][] = Array.from({ length: m }, () => Array(n).fill(false));

    const directions = [[1, 0], [-1, 0], [0, 1], [0, -1]];

    function dfs(r: number, c: number, visited: boolean[][], prevHeight: number) {
        if (r < 0 || c < 0 || r >= m || c >= n || visited[r][c] || heights[r][c] < prevHeight) {
            return;
        }
        visited[r][c] = true;
        for (const [dr, dc] of directions) {
            dfs(r + dr, c + dc, visited, heights[r][c]);
        }
    }

    for (let i = 0; i < m; i++) {
        dfs(i, 0, pacific, heights[i][0]);
        dfs(i, n - 1, atlantic, heights[i][n - 1]);
    }
    for (let i = 0; i < n; i++) {
        dfs(0, i, pacific, heights[0][i]);
        dfs(m - 1, i, atlantic, heights[m - 1][i]);
    }

    const result: number[][] = [];

    for (let r = 0; r < m; r++) {
        for (let c = 0; c < n; c++) {
            if (pacific[r][c] && atlantic[r][c]) {
                result.push([r, c]);
            }
        }
    }

    return result;
}
