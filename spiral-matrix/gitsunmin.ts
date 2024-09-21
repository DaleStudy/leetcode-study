/**
 * https://leetcode.com/problems/spiral-matrix/
 * time complexity : O(m * n)
 * space complexity : O(m * n)
 */

function spiralOrder(matrix: number[][]): number[] {
    let [left, right] = [0, matrix[0].length - 1];
    let [top, bottom] = [0, matrix.length - 1];

    const output = [] as number[];

    while (top <= bottom && left <= right) {
        for (let i = left; i <= right; i++) output.push(matrix[top][i]);
        top++;

        for (let i = top; i <= bottom; i++) output.push(matrix[i][right]);
        right--;

        if (top <= bottom) {
            for (let i = right; i >= left; i--) output.push(matrix[bottom][i]);
            bottom--;
        }

        if (left <= right) {
            for (let i = bottom; i >= top; i--) output.push(matrix[i][left]);
            left++;
        }
    }

    return output;
};
