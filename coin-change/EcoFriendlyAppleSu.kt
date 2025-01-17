package leetcode_study

/*
* 주어진 동전의 종류와 개수를 사용하여 주어진 금액을 만들 때, 중복을 허용한 최소 동전 개수를 구하는 문제
* 너비 우선 탐색을 사용해 문제 해결
* 시간 복잡도: O(n)
* -> queue 자료구조에서 각 동전(n)을 꺼내고 목표 금액(amount == k)까지 도달하는 경우: O(n * k)
* 공간 복잡도: O(k)
* -> 동전 사용 횟수를 저장하는 board의 크기
* */
fun coinChange(coins: IntArray, amount: Int): Int {
    if (amount == 0) return 0
    if (coins.isEmpty() || coins.any { it <= 0 }) return -1

    val board = IntArray(amount + 1) { -1 }
    val queue = ArrayDeque<Int>()

    for (coin in coins) {
        if (coin <= amount) {
            queue.add(coin)
            board[coin] = 1 // 동전 하나로 구성 가능
        }
    }

    while (queue.isNotEmpty()) {
        val currentPosition = queue.pollFirst()
        for (coin in coins) {
            val nextPosition = currentPosition + coin
            if (nextPosition in 1..amount) {
                // 아직 방문하지 않았거나 더 적은 동전으로 구성 가능하면 업데이트
                if (board[nextPosition] == -1 || board[nextPosition] > board[currentPosition] + 1) {
                    queue.add(nextPosition)
                    board[nextPosition] = board[currentPosition] + 1
                }
            }
        }
    }

    return board[amount]
}
