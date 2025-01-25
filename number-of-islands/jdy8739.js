/**
 * @param {character[][]} grid
 * @return {number}
 */
var numIslands = function (grid) {
    const sink = (row, col) => {
        grid[row][col] = '0';

        const neighbor = [
            [row + 1, col], [row, col + 1], [row - 1, col], [row, col - 1]
        ].filter(([y, x]) => {
            return y >= 0 && x >= 0 && y < grid.length && x < grid[0].length;
        }).filter(([y, x]) => {
            return grid[y][x] === '1';
        });

        neighbor.forEach(([y, x]) => {
            const el = grid[y][x];

            if (el === '1') {
                sink(y, x);
            }
        })
    }

    let count = 0;

    for (let i = 0; i < grid.length; i++) {
        for (let j = 0; j < grid[0].length; j++) {

            if (grid[i][j] === '1') {
                count++;
                sink(i, j);
            }
        }
    }

    return count;
};

// 시간복잡도 O(2 * m * n) -> m * n 만큼 반복 + 재귀적으로 방문할 수 있는 셀의 수는 총 m * n 개
// 공간복잡도 O(1) -> 입력 배열을 사용하지 않고 변수만 사용

