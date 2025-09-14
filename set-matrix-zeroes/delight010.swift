class Solution {
    // Time complexity O(MN)
    // Space complexity O(1)
    func setZeroes(_ matrix: inout [[Int]]) {
        var firstRowHasZero = false
        var firstColHasZero = false
        
        for col in 0..<matrix[0].count {
            if matrix[0][col] == 0 {
                firstRowHasZero = true
                break
            }
        }
        
        for row in 0..<matrix.count {
            if matrix[row][0] == 0 {
                firstColHasZero = true
                break
            }
        }
        
        // marking
        for row in 0..<matrix.count {
            for col in 0..<matrix[row].count {
                if matrix[row][col] == 0 {
                    matrix[row][0] = 0
                    matrix[0][col] = 0
                }
            }
        }
        
        // row
        for row in 1..<matrix.count {
            if matrix[row][0] == 0 {
                for col in 0..<matrix[row].count {
                    matrix[row][col] = 0
                }
            }
        }
        
        // column
        for col in 1..<matrix[0].count {
            if matrix[0][col] == 0 {
                for row in 0..<matrix.count {
                    matrix[row][col] = 0
                }
            }
        }
        
        if firstRowHasZero {
            for col in 0..<matrix[0].count {
                matrix[0][col] = 0
            }
        }
        
        if firstColHasZero {
            for row in 0..<matrix.count {
                matrix[row][0] = 0
            }
        }
    }
}
 
