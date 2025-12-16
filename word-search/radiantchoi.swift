class Solution {
    func exist(_ board: [[Character]], _ word: String) -> Bool {
        let target = Array(word)        // Swift String은 인덱스를 통한 접근에 어려움이 있어, Array로 변환
        let threshold = target.count    
        var board = board               // inout 파라미터로 사용하기 위해 변수로 변환

        for i in 0..<board.count {
            for j in 0..<board[i].count {
                // 백트래킹 순회 함수
                // 조건에 맞는 결과가 있으면 바로 true 반환 - early return
                if traverse(&board, 0, i, j, threshold, target) {
                    return true
                }
            }
        }

        // 모든 좌표를 순회한 후에도 매칭되는 결과가 없으면 false 반환
        return false
    }

    // threshold를 target.count로 사용할 수 있으나, 매번 계산하지 않기 위해 부모 함수에서 한 번만 계산하고 파라미터에 포함
    func traverse(_ board: inout [[Character]], _ checked: Int, _ row: Int, _ col: Int, _ threshold: Int, _ target: [Character]) -> Bool {
        // 지금까지 체크한 글자 수가 단어의 총 글자 수와 같다면, true 반환
        // 아래의 조건에 따라 매칭되지 않는다면 그 이전에 false가 반환되었을 것이기 때문
        if checked == threshold {
            return true
        }

        // 현재 좌표가 보드의 범위를 벗어난다면 false 반환
        guard (0..<board.count) ~= row && (0..<board[0].count) ~= col else {
            return false
        }

        // 현재 좌표의 글자가 단어의 현재 체크해야 할 글자와 일치하지 않는다면 바로 false 반환
        guard board[row][col] == target[checked] else {
            return false
        }
        
        // 백트래킹 스텝 1: 현재 좌표의 글자를 임시 변수에 저장하고, 현재 좌표의 글자를 "#"로 변경
        let temp = board[row][col]
        board[row][col] = "#"

        // 백트래킹 스텝 2: 현재 좌표의 상하좌우를 순회하며, 매칭되는 결과가 있으면 true 반환
        let result = traverse(&board, checked + 1, row + 1, col, threshold, target)
        || traverse(&board, checked + 1, row - 1, col, threshold, target)
        || traverse(&board, checked + 1, row, col + 1, threshold, target)
        || traverse(&board, checked + 1, row, col - 1, threshold, target)

        // 백트래킹 스텝 3: 현재 좌표의 글자를 원래 값으로 복구
        board[row][col] = temp

        return result
    }
}
