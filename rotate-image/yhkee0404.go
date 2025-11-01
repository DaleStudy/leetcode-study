func rotate(matrix [][]int)  {
    for i := range len(matrix) {
        for j := i + 1; j != len(matrix[i]); j++ { // T(n) = O(n)
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        }
    }
    for _, row := range matrix {
        for i, j := 0, len(row) - 1; i < j; {
            row[i], row[j] = row[j], row[i]
            i++
            j--
        } 
    }
}
