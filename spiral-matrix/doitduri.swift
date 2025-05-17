class Solution {
    func spiralOrder(_ matrix: [[Int]]) -> [Int] {
        guard !matrix.isEmpty else { return [] }
        
        var answer: [Int] = []
        
        var top = 0
        var bottom = matrix.count - 1
        var left = 0
        var right = matrix[0].count - 1
        
        while top <= bottom && left <= right {
            for i in left...right {
                answer.append(matrix[top][i])
            }
            top += 1
            
            if top <= bottom {
                for i in top...bottom {
                    answer.append(matrix[i][right])
                }
            }
            right -= 1
            
            if top <= bottom && left <= right {
                for i in stride(from: right, through: left, by: -1) {
                    answer.append(matrix[bottom][i])
                }
                bottom -= 1
            }
            
            if left <= right && top <= bottom {
                for i in stride(from: bottom, through: top, by: -1) {
                    answer.append(matrix[i][left])
                }
                left += 1
            }
        }
        
        return answer
    }
}
