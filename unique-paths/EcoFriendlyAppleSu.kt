package leetcode_study

/*
* 주어진 m,n size board 위에서 좌측 위부터 우측 아래까지 도착하는 Unique path의 개수를 구하는 방법 (m = row size, n = col size)
* 움직일 수 있는 방향이 아래와 오른쪽으로 정해저 있는 상황에서 다음 칸으로 갈 수 있는 방법은 아래와 같음
* board[i][j] = board[i][j-1] + board[i-1][j]
* 시간 복잡도: O(mn)
* -> board를 순회하며 unique path를 구하는 과정
* 공간 복잡도: O(mn)
* -> m, n을 사용해 board를 구성
* */
fun uniquePaths(m: Int, n: Int): Int {
    val board = Array(m) { IntArray(n) { 0 } }

    for (i in IntRange(0, m-1)) {
        board[i][0] = 1
    }
    for (i in IntRange(0, n-1)) {
        board[0][i] = 1
    }

    for (i in 1 until m) {
        for (j in 1 until n) {
            board[i][j] = board[i][j-1] + board[i-1][j]
        }
    }

    return board[m-1][n-1]
}
