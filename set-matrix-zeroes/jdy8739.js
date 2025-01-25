/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var setZeroes = function (matrix) {
    const coord = [];

    for (let i = 0; i < matrix.length; i++) {
        for (let j = 0; j < matrix[i].length; j++) {

            const num = matrix[i][j];

            if (num === 0) {
                coord.push({ y: i, x: j });
            }
        }
    }

    for (let k = 0; k < coord.length; k++) {
        const { y } = coord[k];

        for (let j = 0; j < matrix[0].length; j++) {
            matrix[y][j] = 0;
        }
    }

    for (let l = 0; l < coord.length; l++) {
        const { x } = coord[l];

        for (let j = 0; j < matrix.length; j++) {
            matrix[j][x] = 0;
        }
    }
};

// 시간복잡도 O(n * m)
// 공간복잡도 O(n * m)

