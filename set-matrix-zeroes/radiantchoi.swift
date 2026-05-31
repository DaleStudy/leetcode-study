class Solution {
    func setZeroes(_ matrix: inout [[Int]]) {
        // 원래 0이었던 것의 주변을 모두 0으로 만들되, 기존에 0이었던 것들은 독립적으로 영향력을 행사해야 함
        // 주변으로 먼저 0으로 만들어 버리면, flood fill 형태로 모든 원소가 0이 되어버림
        // 따라서 변경해야 할 값을 미리 "마크해 두고", 이후 이 마크해 둔 값을 0으로 바꾸는 전략 선택

        // 원소 값의 범위: -2^31보다 크거나 같고, 2^31 - 1보다 작거나 같음
        // 따라서 범위에 포함되지 않는 2^32를 사용하여 계산 - 일부 언어에서는 overflow 발생 가능
        let threshold = Int(pow(2.0, 32))

        for i in 0..<matrix.count {
            for j in 0..<matrix[i].count {
                if matrix[i][j] == 0 {
                    // 상, 하, 좌, 우를 각각 전담해 마크하는 함수들
                    // 해당하는 자리의 중복 조회를 줄이기 위해 각각의 인덱스에 미리 튜닝을 가해서 투입
                    traverseRowNegative(i-1, j, &matrix, threshold)
                    traverseRowPositive(i+1, j, &matrix, threshold)
                    traverseColumnNegative(i, j-1, &matrix, threshold)
                    traverseColumnPositive(i, j+1, &matrix, threshold)
                }
            }
        }

        // 전체 매트릭스를 순회하면서 마크해뒀던 값을 0으로 치환
        for i in 0..<matrix.count {
            for j in 0..<matrix[i].count {
                if matrix[i][j] == threshold {
                    matrix[i][j] = 0
                }
            }
        }
    }

    func traverseRowNegative(_ row: Int, _ col: Int, _ matrix: inout [[Int]], _ threshold: Int) {
        guard (0..<matrix.count) ~= row else { return }

        // 이미 0이었던 원소라면 건드리지 말고, 그렇지 않다면 threshold로 마크
        // 아래 모든 함수에서도 동일한 원리로 동작
        if matrix[row][col] != 0 {
            matrix[row][col] = threshold
        }

        traverseRowNegative(row - 1, col, &matrix, threshold)
    }

    func traverseRowPositive(_ row: Int, _ col: Int, _ matrix: inout [[Int]], _ threshold: Int) {
        guard (0..<matrix.count) ~= row else { return }

        if matrix[row][col] != 0 {
            matrix[row][col] = threshold
        }

        traverseRowPositive(row + 1, col, &matrix, threshold)
    }

    func traverseColumnNegative(_ row: Int, _ col: Int, _ matrix: inout [[Int]], _ threshold: Int) {
        guard (0..<matrix[row].count) ~= col else { return }

        if matrix[row][col] != 0 {
            matrix[row][col] = threshold
        }

        traverseColumnNegative(row, col - 1, &matrix, threshold)
    }

    func traverseColumnPositive(_ row: Int, _ col: Int, _ matrix: inout [[Int]], _ threshold: Int) {
        guard (0..<matrix[row].count) ~= col else { return }

        if matrix[row][col] != 0 {
            matrix[row][col] = threshold
        }

        traverseColumnPositive(row, col + 1, &matrix, threshold)
    }
}
