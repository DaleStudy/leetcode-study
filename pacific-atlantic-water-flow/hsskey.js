/**
 * @param {number[][]} heights
 * @return {number[][]}
 */
var pacificAtlantic = function(heights) {
    const ROWS = heights.length;
    const COLS = heights[0].length;

    const pac = new Set();
    const atl = new Set();

    const dfs = (r, c, visit, prevHeight) => {
        const key = `${r},${c}`;
        if (
            visit.has(key) ||
            r < 0 || c < 0 || r >= ROWS || c >= COLS ||
            heights[r][c] < prevHeight
        ) {
            return;
        }

        visit.add(key);

        dfs(r + 1, c, visit, heights[r][c]);
        dfs(r - 1, c, visit, heights[r][c]);
        dfs(r, c + 1, visit, heights[r][c]);
        dfs(r, c - 1, visit, heights[r][c]);
    };

    for (let c = 0; c < COLS; c++) {
        dfs(0, c, pac, heights[0][c]);               // Top row (Pacific)
        dfs(ROWS - 1, c, atl, heights[ROWS - 1][c]);  // Bottom row (Atlantic)
    }

    for (let r = 0; r < ROWS; r++) {
        dfs(r, 0, pac, heights[r][0]);               // Left col (Pacific)
        dfs(r, COLS - 1, atl, heights[r][COLS - 1]); // Right col (Atlantic)
    }

    const res = [];
    for (let r = 0; r < ROWS; r++) {
        for (let c = 0; c < COLS; c++) {
            const key = `${r},${c}`;
            if (pac.has(key) && atl.has(key)) {
                res.push([r, c]);
            }
        }
    }

    return res;
};
