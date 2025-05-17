/*
    (0, 0)  0~m, 0~n 
    (1, 1) (0~m, 1) (1, 0~n)

    time complexity : O(m * n)
    space complexity : O(m * n)
*/
function setZeroes(matrix: number[][]): void {
    const rows = matrix.length
    const cols = matrix[0].length
    const zeroPosition = []
    for (let r = 0; r < rows; r++) {
        for (let c = 0; c < cols; c++) {
            if (matrix[r][c] === 0) {
                zeroPosition.push([r,c])
            }
        }
    }
    
    for (let m = 0; m < zeroPosition.length; m++) {
        const r = zeroPosition[m][0]
        const c = zeroPosition[m][1]
        matrix[r].fill(0)
        for (let i = 0; i < rows; i++) {
            matrix[i][c] = 0
        }
    }
};
