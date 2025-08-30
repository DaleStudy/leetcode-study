class Solution {
    func spiralOrder(_ matrix: [[Int]]) -> [Int] {
        var answer: [Int] = []
        var top = 0
        var bottom = matrix.endIndex - 1
        var left = 0
        var right = matrix[0].endIndex - 1
        while top <= bottom && left <= right {
            for column in left...right {
                answer.append(matrix[top][column])
            }
            top += 1
            
            if top <= bottom {
                for row in top...bottom {
                    answer.append(matrix[row][right])
                }
            }
            right -= 1
            
            if top <= bottom {
                for column in stride(from: right, through: left, by: -1) {
                    answer.append(matrix[bottom][column])
                }
            }
            bottom -= 1
            
            if left <= right {
                for row in stride(from: bottom, through: top, by: -1) {
                    answer.append(matrix[row][left])
                }
            }
            left += 1
        }
        return answer
    }
}
 
