package leetcode_study


/*
* dfs로 문제 해결
* 정해진 순서의 단어를 처리하는 부분에서 대부분의 시간 사용
* 시간 복잡도: O(m *n)
* -> 주어진 배열에서 첫 번째 글자를 찾는 반복문: O(m *n)
* -> 최악의 경우 모든 칸을 방문 처리(dfs): O(m *n)
* --> O(m *n) + O(m *n) == O(m *n)
* 공간 복잡도: O(m *n)
* -> 재귀 호출 스택 공간 dfs 함수에서 최악의 경우 필요한 스택 공간: O(m *n)
* */
val dx = listOf(0, 1, -1, 0)
val dy = listOf(1, 0, 0, -1)

fun exist(board: Array<CharArray>, word: String): Boolean {
    val rowSize = board.size
    val colSize = board[0].size
    val visited = Array(rowSize) { BooleanArray(colSize) }

    // 모든 위치에서 DFS 탐색 시작
    for (i in board.indices) {
        for (j in board[0].indices) {
            if (board[i][j] == word[0] && dfs(board, word, i, j, 0, visited)) {
                return true
            }
        }
    }
    return false
}

fun dfs(board: Array<CharArray>, word: String, x: Int, y: Int, index: Int, visited: Array<BooleanArray>): Boolean {
    // 탐색 종료 조건
    if (index == word.length) return true
    if (x !in board.indices || y !in board[0].indices || visited[x][y] || board[x][y] != word[index]) return false

    // 현재 위치 방문 처리
    visited[x][y] = true

    // 4방향으로 탐색
    for (i in 0..3) {
        val nx = x + dx[i]
        val ny = y + dy[i]
        if (dfs(board, word, nx, ny, index + 1, visited)) {
            return true
        }
    }

    // 방문 복구
    visited[x][y] = false
    return false
}
