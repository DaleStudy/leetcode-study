package leetcode_study

/*
* 주어진 숫자 배열에서 존재하지 않은 수 판별하는 문제
* 0부터 n의 범위에서 모든 수는 유일하게 존재
* 시간 복잡도: O(n)
* -> nums 배열을 순회하며, 각 요소에 대해 board 배열에 값을 설정: O(n)
* -> board 배열을 순회하며, 값이 0인 인덱스 검색: O(n)
* --> O(n) + O(n) = O(n)
* 공간 복잡도: O(n)
* -> 입력 배열 nums의 크기가 n일 때, board 배열의 크기 n + 1: O(n)
* */
fun missingNumber(nums: IntArray): Int {
    val size = nums.size
    val board = IntArray(size+1)
    for (index in nums.indices) {
        board[nums[index]] = 1
    }

    for (i in board.indices) {
        if (board[i] == 0) {
            return i
        }
    }
    return 0
}
