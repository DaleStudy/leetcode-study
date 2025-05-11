function spiralOrder(matrix: number[][]): number[] {
    const m = matrix.length
    const n = matrix[0].length
    const size = m * n
    let traversed = 0
    let top = 0
    let bottom = m - 1
    let left = 0
    let right = n - 1
    const output = []

    while (traversed < size) {
        for (let i = left; traversed < size && i <= right; i++, traversed++) {
            output.push(matrix[top][i])
        }
        top++

        for (let i = top; traversed < size && i <= bottom; i++, traversed++) {
            output.push(matrix[i][right])
        }
        right--
                
        for (let i = right; traversed < size && i >= left; i--, traversed++) {
            output.push(matrix[bottom][i])
        }
        bottom--

        for (let i = bottom; traversed < size && i >= top; i--, traversed++) {
            output.push(matrix[i][left])
        }
        left++
    }
    return output
};
