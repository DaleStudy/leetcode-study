package leetcode_study

/*
* 주어진 범위 값 병합 문제
* */

/*
* 첫 번째 풀이. 틀림
* 범위 안에 속하는 모든 값을 Set 자료구조에 넣고 제일 큰 숫자 만큼의 Boolean Array를 만든 후 방문처리하는 방식으로 접근
* 예외 케이스
* intervals = [[1,4],[5,6]] 일 때,
* 연속된 값으로 인식해 답을 [[1,6]]로 도출. 올바른 답은 [[1,4],[5,6]]
* */
fun merge01(intervals: Array<IntArray>): Array<IntArray> {
    val tempSet = mutableSetOf<Int>()
    var maxValue = Int.MIN_VALUE

    for (interval in intervals) {
        val leftValue = interval[0]
        val rightValue = interval[1]
        maxValue = max(maxValue, rightValue)
        for (value in leftValue until  rightValue + 1) {
            tempSet.add(value)
        }
    }

    val checkVisited = BooleanArray(maxValue + 1) { false }
    for (value in tempSet) {
        checkVisited[value] = true
    }

    val result = mutableListOf<IntArray>()
    var start: Int? = null

    for (i in checkVisited.indices) {
        if (checkVisited[i]) {
            if (start == null) start = i // 시작점 저장
            // 연속된 값이 true일 경우엔 넘어감
        } else {
            if (start != null) {
                result.add(intArrayOf(start, i - 1)) // [start, end] 추가
                start = null
            }
        }
    }
    if (start != null) {
        result.add(intArrayOf(start, checkVisited.lastIndex))
    }

    return result.toTypedArray()
}

/*
* 주어진 범위 값을 정렬하고 순회하면서 병합 여부 판단
* 시간 복잡도: O(n log n)
* -> 첫 번째 원소 기준으로 TimSort 알고리즘을 사용한 정렬: O(n log n)
* -> 주어진 interval 만큼 순회해 계산: O(n)
* 공간 복잡도: O(n)
* -> 첫 번째 원소로 정렬된 sortedIntervals를 담는 공간: O(n)
* */
fun merge02(intervals: Array<IntArray>): Array<IntArray> {
    if (intervals.isEmpty()) return intervals

    // 시작점 기준으로 정렬
    val sortedIntervals = intervals.sortedBy { it[0] }

    val result = mutableListOf<IntArray>()
    var currentInterval = sortedIntervals[0]

    for (i in 1 until sortedIntervals.size) {
        val interval = sortedIntervals[i]
        // 겹치는 경우: 현재 구간의 끝이 다음 구간의 시작보다 크거나 같으면 merge
        if (currentInterval[1] >= interval[0]) {
            currentInterval[1] = maxOf(currentInterval[1], interval[1])
        } else {
            // 겹치지 않으면 현재 구간을 결과에 추가하고, 새 구간으로 변경
            result.add(currentInterval)
            currentInterval = interval
        }
    }
    // 마지막 구간 추가
    result.add(currentInterval)

    return result.toTypedArray()
}
