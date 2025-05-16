/**
 * @param {character[][]} grid
 * @return {number}
 */
var numIslands = function(grid) {
    if (!grid.length) return 0;

    const rows = grid.length;
    const cols = grid[0].length;
    const visit = new Set();
    let islands = 0;

    const bfs = (r, c) => {
        const queue = [];
        queue.push([r, c]);
        visit.add(`${r},${c}`);

        while (queue.length) {
            const [row, col] = queue.shift();
            const directions = [
                [1, 0],
                [-1, 0],
                [0, 1],
                [0, -1],
            ];

            for (const [dr, dc] of directions) {
                const newRow = row + dr;
                const newCol = col + dc;

                if (
                    newRow >= 0 &&
                    newRow < rows &&
                    newCol >= 0 &&
                    newCol < cols &&
                    grid[newRow][newCol] === '1' &&
                    !visit.has(`${newRow},${newCol}`)
                ) {
                    queue.push([newRow, newCol]);
                    visit.add(`${newRow},${newCol}`);
                }
            }
        }
    };

    for (let r = 0; r < rows; r++) {
        for (let c = 0; c < cols; c++) {
            if (grid[r][c] === '1' && !visit.has(`${r},${c}`)) {
                bfs(r, c);
                islands += 1;
            }
        }
    }

    return islands;
};
