// 시간복잡도: O(n * m)
// 공간복잡도: O(n * m)

const dr = [1,-1,0,0]
const dc = [0,0,-1, 1]

const isValidMove = (grid, n_row, n_col) => {
    return n_row >= 0 && n_row < grid.length && n_col >= 0 && n_col < grid[0].length && grid[n_row][n_col] !== '0'
}


/**
 * @param {character[][]} grid
 * @return {number}
 */
var numIslands = function(grid) {
    let islandCount = 0;

    const bfs = (row, col) => {
        const que = [[row,col]]

        while (que.length) {
            const [row, col] = que.pop()

            for (let i = 0 ; i < dr.length; i++) {
                const n_row = row + dr[i]
                const n_col = col + dc[i]

                if (isValidMove(grid, n_row, n_col)) {
                    que.push([n_row, n_col])
                }
            }

            grid[row][col] = '0'

        }

        islandCount += 1
    }


    for (let row = 0; row < grid.length; row++) {
        for (let col = 0; col < grid[row].length; col++) {
            if (grid[row][col] !== '0') bfs(row, col)
        }
    }


    return islandCount
};

console.log(numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))
