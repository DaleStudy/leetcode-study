/**
 Do not return anything, modify matrix in-place instead.
 */
/**
 * 90도 회전시키기
 * 알고리즘 복잡도
 * - 시간 복잡도: O(n2)
 * - 공간 복잡도: O(1)
 * @param matrix
 */
function rotate(matrix: number[][]): void {
    let n = matrix.length;

    // 0,0 -> 2,0
    // 1,0 -> 2,1
    // 2,0 -> 2,2

    // 0,1 -> 1,0
    // 1,1 -> 1,1
    // 2,1 -> 1,2

    // 0,2 -> 0,0
    // 1,2 -> 0,1
    // 2,2 -> 0,2

    // 1 2 3
    // 4 5 6
    // 7 8 9

    // 1 4 7
    // 2 5 8
    // 3 6 9

    // 7 4 1
    // 8 5 2
    // 9 6 3

    // 1. 행과 열을 바꿈(행과 열의 전치)
    for (let i = 0; i < n; i++) {
        for (let j = i; j < n; j++) {
            // 대각선을 기준으로 대칭
            if (i !== j) {
                const temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
        }
    }

    // 2. 각 행을 좌우로 뒤집기(= 90도 회전)
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < Math.floor(n / 2); j++) {
            const temp = matrix[i][j];
            matrix[i][j] = matrix[i][n - 1 - j];
            matrix[i][n - 1 - j] = temp;
        }
    }
}
