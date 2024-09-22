// 시간복잡도 O(n * m)
// 공간복잡도 O(n * m)

const isVisited = (matrix, row, col) => {
    return matrix[row][col] === '#'
}

/**
 * @param {number[][]} matrix
 * @return {number[]}
 */
var spiralOrder = function(matrix) {
    const result = []

    const colLen = matrix[0].length;
    const rowLen = matrix.length

    let direction = 'right'
    let row = 0;
    let col = 0;
    while (result.length < colLen * rowLen ) {
        result.push(matrix[row][col])
        matrix[row][col] = '#'

        if (direction === 'right') {
            if (isVisited(matrix, row, col+1) || col === colLen - 1) {
                direction = 'down'
                row++
            } else {
                col++
            }
        } else if (direction === 'down') {
            if ((row + 1 < rowLen &&  isVisited(matrix, row+1, col) || row === rowLen - 1)) {
                direction = 'left'
                col--
            } else {
                row++
            }
        } else if (direction === 'left') {
            if ((col > 0 && isVisited(matrix, row, col-1) || col === 0)) {
                direction = 'up'
                row--
            } else {
                col--
            }
        } else if (direction === 'up') {
            if ( (row > 0 && isVisited(matrix,row-1, col))) {
                direction = 'right'
                col++
            } else {
                row--
            }
        }

    }

    return result
};



console.log(spiralOrder([
    [1,2,3],
    [4,5,6],
    [7,8,9]])) // [1,2,3,6,9,8,7,4,5]

