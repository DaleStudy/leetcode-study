class Solution {
    func setZeroes(_ matrix: inout [[Int]]) {
    let m = matrix.count
    let n = matrix[0].count
    
    var firstRowHasZero = false
    var firstColHasZero = false
    
    for i in 0..<m {
        if matrix[i][0] == 0 {
            firstColHasZero = true
            break
        }
    }
    
    for j in 0..<n {
        if matrix[0][j] == 0 {
            firstRowHasZero = true
            break
        }
    }
    
    for i in 1..<m {
        for j in 1..<n {
            if matrix[i][j] == 0 {
                matrix[i][0] = 0
                matrix[0][j] = 0
            }
        }
    }
    
    for i in 1..<m {
        if matrix[i][0] == 0 {
            for j in 1..<n {
                matrix[i][j] = 0
            }
        }
    }
    
    for j in 1..<n {
        if matrix[0][j] == 0 {
            for i in 1..<m {
                matrix[i][j] = 0
            }
        }
    }
    
    if firstRowHasZero {
        for j in 0..<n {
            matrix[0][j] = 0
        }
    }
    
    if firstColHasZero {
        for i in 0..<m {
            matrix[i][0] = 0
        }
    }
    }
}
