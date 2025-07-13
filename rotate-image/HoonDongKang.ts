/**
 * [Problem]: [48] Rotate Image
 * (https://leetcode.com/problems/rotate-image/)
 */
/**
 Do not return anything, modify matrix in-place instead.
 */
// 시간복잡도 O(n^2)
// 공간복잡도 O(1)
function rotate(matrix: number[][]): void {
    const length = matrix.length;

    for (let i = 0; i < length; i++) {
        for (let j = i + 1; j < length; j++) {
            [matrix[i][j], matrix[j][i]] = [matrix[j][i], matrix[i][j]];
        }
    }

    for (let i = 0; i < length; i++) {
        matrix[i].reverse();
    }
}
