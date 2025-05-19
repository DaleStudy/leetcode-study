/**
 * [Problem]: [200] Number of Islands
 * (https://leetcode.com/problems/number-of-islands/description/)
 */
function numIslands(grid: string[][]): number {
    //시간복잡도 O(n)
    //공간복잡도 O(n)
    function dfsFunc(grid: string[][]): number {
        let rows = grid.length;
        let cols = grid[0].length;
        let count = 0;

        for (let i = 0; i < rows; i++) {
            for (let j = 0; j < cols; j++) {
                if (grid[i][j] === "1") {
                    count++;
                    traveling(i, j);
                }
            }
        }

        function traveling(i: number, j: number) {
            grid[i][j] = "#";

            [
                [i - 1, j],
                [i + 1, j],
                [i, j - 1],
                [i, j + 1],
            ].forEach(([r, c]) => {
                if (0 <= r && r < rows && 0 <= c && c < cols) {
                    if (grid[r][c] === "1") traveling(r, c);
                }
            });
        }

        return count;
    }

    //시간복잡도 O(n)
    //공간복잡도 O(n)
    function stackFunc(grid: string[][]): number {
        let rows = grid.length;
        let cols = grid[0].length;
        let count = 0;

        for (let i = 0; i < rows; i++) {
            for (let j = 0; j < cols; j++) {
                if (grid[i][j] === "1") {
                    count++;
                    traveling(i, j);
                }
            }
        }

        function traveling(i: number, j: number) {
            let stack = [[i, j]];

            while (stack.length) {
                let [r, c] = stack.pop()!;
                grid[r][c] = "#";

                [
                    [r - 1, c],
                    [r + 1, c],
                    [r, c - 1],
                    [r, c + 1],
                ].forEach(([r, c]) => {
                    if (0 <= r && r < rows && 0 <= c && c < cols) {
                        if (grid[r][c] === "1") stack.push([r, c]);
                    }
                });
            }
        }

        return count;
    }

    return stackFunc(grid);
}
