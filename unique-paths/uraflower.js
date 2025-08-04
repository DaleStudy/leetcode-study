/**
 * (0,0)에서 (m,n)에 도달할 수 있는 방법의 수를 반환하는 함수
 * @param {number} m
 * @param {number} n
 * @return {number}
 */
const uniquePaths = function (m, n) {
    const grid = Array.from({length: m}, () => Array(n).fill(0));
    let r = 0;
    let c = 0;
    const queue = [[r, c]];
    grid[r][c] = 1;

    while (queue.length) {
        const [x, y] = queue.shift();

        if (x === m - 1 && y === n - 1) {
            continue;
        }

        if (0 <= x + 1 && x + 1 < m) {
            if (grid[x+1][y] === 0) queue.push([x + 1, y]);
            grid[x+1][y] += grid[x][y];
        }

        if (0 <= y + 1 && y + 1 < n) {
            if (grid[x][y+1] === 0) queue.push([x, y + 1]);
            grid[x][y+1] += grid[x][y];
        }
    }

    return grid[m-1][n-1];
};

// 시간복잡도: O(m * n)
// 공간복잡도: O(m * n)
