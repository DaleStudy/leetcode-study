/**
 * 주어진 2차원 격자에서 섬의 개수를 반환하는 함수
 * 시간복잡도: O(m * n) (모든 원소를 순회해야 함)
 * 공간복잡도: O(m * n) (bfs의 공간복잡도에 따름)
* @param {character[][]} grid
 * @return {number}
 */
const numIslands = function (grid) {
    let num = 0;

    for (let r = 0; r < grid.length; r++) {
        for (let c = 0; c < grid[0].length; c++) {
            if (grid[r][c] === '1') {
                bfs(grid, r, c);
                num += 1;
            }
        }
    }

    return num;
};

// grid의 주어진 좌표에서 bfs를 수행해 방문했음을 표시
// 시간복잡도: O(m * n) (최악의 경우 모든 원소 순회)
// 공간복잡도: O(m * n) (최악의 경우 queue에 모든 원소 저장)
function bfs(grid, x, y) {
    const queue = [[x, y]];
    const dx = [0, 0, 1, -1];
    const dy = [1, -1, 0, 0];
    const rows = grid.length;
    const cols = grid[0].length;

    while (queue.length) {
        const [r, c] = queue.shift();

        for (let i = 0; i < 4; i++) {
            const nr = r + dx[i];
            const nc = c + dy[i];

            if (0 <= nr && nr < rows && 0 <= nc && nc < cols && grid[nr][nc] === '1') {
                queue.push([nr, nc]);
                grid[nr][nc] = '0';
            }
        }
    }
}
