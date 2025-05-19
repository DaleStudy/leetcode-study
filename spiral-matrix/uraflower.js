/**
 * 주어진 행렬을 나선형(우-하-좌-상)으로 순회한 결과를 반환하는 함수
 * @param {number[][]} matrix
 * @return {number[]}
 */
const spiralOrder = function (matrix) {
    const rows = matrix.length;
    const cols = matrix[0].length;
    let r = 0;
    let c = 0;
    let dr = 0; // 0, 1, 0, -1
    let dc = 1; // 1, 0, -1, 0

    const output = [];

    for (let i = 0; i < rows * cols; i++) {
        output.push(matrix[r][c]);
        matrix[r][c] = null;

        // 방향을 전환해야 하는 경우
        if (!(0 <= r + dr && r + dr < rows && 0 <= c + dc && c + dc < cols) || matrix[r + dr][c + dc] === null) {
            [dr, dc] = [dc, -dr];
        }

        r += dr;
        c += dc;
    }

    return output;
};

// 시간복잡도: O(r * c)
// 공간복잡도: O(1)
