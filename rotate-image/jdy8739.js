/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var rotate = function (matrix) {
    const rotateMatrix = (matrix, start) => {
        const length = matrix.length;

        const end = length - 1 - start;

        if (end <= start) {
            return;
        }

        for (let i = start; i < end; i++) {
            const temp = matrix[start][i];

            const target = length - 1 - i;

            matrix[start][i] = matrix[target][start];
            matrix[target][start] = matrix[end][target];
            matrix[end][target] = matrix[i][end];
            matrix[i][end] = temp;
        }

        rotateMatrix(matrix, start + 1);
    }

    rotateMatrix(matrix, 0);
};

// 시간복잡도 O(n^2)
// 공간복잡도 O(l) -> 재귀호출 스택이 최대 매트릭스의 길이 / 2로 최대 쌓이므로
