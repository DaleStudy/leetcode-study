/*
    time complexity : O(m * n)
    space complexity : O(m)
*/
function numIslands(grid: string[][]): number {
    const rows = grid.length
    const cols = grid[0].length
    const direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    let islands = 0
    for (let r = 0; r < rows; r++) {
        for (let c = 0; c < cols; c++) {
            if (grid[r][c] === '1') {
                islands += 1
                const queue = new Array()

                grid[r][c] = '0'
                queue.push([r, c])
                while (queue.length > 0) {
                    let curr = queue.shift()
                    for (const dir of direction) {
                        let dr = curr[0] + dir[0]
                        let dc = curr[1] + dir[1]
                        if (dr < 0 || dr >= rows || dc < 0 || dc >= cols || grid[dr][dc] === '0') continue
                        grid[dr][dc] = '0'
                        queue.push([dr, dc])
                    }
                }
            }
        }
    }
    return islands
};
