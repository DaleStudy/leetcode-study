// 시간복잡도: O((n * m) * (n + m))
// 공간복잡도: O(n * m)

/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var setZeroes = function(matrix) {
    const zeroIndexes = []

    for (let row = 0; row < matrix.length; row++) {
        for (let col = 0; col < matrix[row].length; col++) {
            if (matrix[row][col] === 0) {
                zeroIndexes.push([row,col])
            }
        }
    }

    while (zeroIndexes.length) {
        const [row, col] = zeroIndexes.pop()

        for (let i = 0; i < matrix[0].length; i++) {
            matrix[row][i] = 0
        }

        for (let j = 0; j < matrix.length; j++) {
            matrix[j][col] = 0
        }

    }

    return matrix
};

console.log(setZeroes([
    [1,1,1],
    [1,0,1],
    [1,1,1]]))
console.log(setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))
