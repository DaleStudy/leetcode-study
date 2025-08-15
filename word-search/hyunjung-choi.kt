/*
 * 시간 복잡도 (R=행, C=열, N=R*C, L=word.length)
 * - 모든 칸(N개)에서 시작 가능.
 * - DFS 한 단계에서 최대 4방향, 다음 단계부터는 되돌아갈 수 없으므로 최대 3방향으로 분기.
 * - 최악: N * (4 * 3^(L-1)) = O(R*C*3^L).
 *
 * 공간 복잡도
 * - visited 배열: O(R*C)
 * - 재귀 콜스택: 경로 길이 최대 L → O(L)
 * - 총합: O(R*C + L) (최악 기준은 O(R*C))
 */

class Solution {
    fun exist(board: Array<CharArray>, word: String): Boolean {
        if (word.isEmpty()) return true

        val rows = board.size
        val cols = board.firstOrNull()?.size ?: return false
        val visited = Array(rows) { BooleanArray(cols) }
        val directions = arrayOf(1 to 0, -1 to 0, 0 to 1, 0 to -1)

        fun dfs(r: Int, c: Int, index: Int): Boolean {
            if (index == word.length) return true
            if (r !in 0 until rows || c !in 0 until cols) return false
            if (visited[r][c] || board[r][c] != word[index]) return false

            visited[r][c] = true
            val found = directions.any { (dr, dc) -> dfs(r + dr, c + dc, index + 1) }
            visited[r][c] = false
            return found
        }

        return board.indices.any { r ->
            board[0].indices.any { c ->
                board[r][c] == word[0] && dfs(r, c, 0)
            }
        }
    }
}
