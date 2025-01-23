package leetcode_study

/*
* board에서 0이 발견 되었을 때, 기준 row, column을 모두 0으로 변경하는 문제
* Set 자료구조를 사용해 중복을 없애고 순회하여 문제 해결
* 시간 복잡도: O(n^2) (정확히는 O(row * col))
* -> board의 row, col을 순회해 0을 찾는 과정
* -> set으로 중복을 제거한 row을 순회해 board의 값을 0으로 변경하는 과정
* -> set으로 중복을 제거한 column을 순회해 board의 값을 0으로 변경하는 과정
* 공간 복잡도: O(1)
* -> 중복을 제거한 rowSet, columnSet을 저장하는 공간
* */
fun setZeroes(matrix: Array<IntArray>): Unit {
    val rowSet = mutableSetOf<Int>()
    val colSet = mutableSetOf<Int>()

    val rowSize = matrix.size
    val colSize = matrix[0].size

    // find row col
    for (row in matrix.indices) {
        for (col in matrix[0].indices) {
            if (matrix[row][col] == 0) {
                rowSet.add(row)
                colSet.add(col)
            }
        }
    }

    if (rowSet.size == 0 && colSet.size == 0) return

    for (row in rowSet) {
        for (index in IntRange(0, colSize - 1)) {
            matrix[row][index] = 0
        }
    }

    for (col in colSet) {
        for(index in IntRange(0, rowSize - 1)) {
            matrix[index][col] = 0
        }
    }
}
