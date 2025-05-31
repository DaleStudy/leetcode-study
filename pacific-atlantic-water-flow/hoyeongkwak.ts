/*
Time complexity : O(m * n)
Space complexity : O(m * n)
*/
function pacificAtlantic(heights: number[][]): number[][] {
    const m = heights.length
    const n = heights[0].length
    const pacific: boolean[][] = Array(m).fill(null).map(() => Array(n).fill(false))
    const atlantic: boolean[][] = Array(m).fill(null).map(() => Array(n).fill(false))

    const dfs = (row: number, col: number, visited: boolean[][], prevH: number): void => {
        if (row < 0 || row >= m || col < 0 || col >= n || visited[row][col] || heights[row][col] < prevH) {
            return
        }
        visited[row][col] = true
        const directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for (const [dr, dc] of directions) {
            dfs(row + dr, col + dc, visited, heights[row][col])
        }
    }

    for (let row = 0; row < m; row++) {
        dfs(row, 0, pacific, heights[row][0])
        
    }

    for (let col = 0; col < n; col++) {
        dfs(0, col, pacific, heights[0][col])
    }

     for (let row = 0; row < m; row++) {
        dfs(row, n - 1, atlantic, heights[row][n - 1])
    }

    for (let col = 0; col < n; col++) {
        dfs(m - 1, col, atlantic, heights[m - 1][col])
    }

    const result: number[][] = []
    for (let row = 0; row < m; row++) {
        for (let col = 0; col < n; col++) {
            if (pacific[row][col] && atlantic[row][col]) {
                result.push([row, col])
            }
        }
    }
    return result
};
