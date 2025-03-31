package leetcode_study

/*
* 겹치는 시간 없이 미팅룸 시간을 잡을 수 있는지 판단하는 문제
* 시작 시간을 기준으로 정렬한 후 종료 시간과 다음 미팅의 시간을 비교해 겹치는 부분이 있다면 잡을 수 없는 미팅 룸으로 판단
*
* 시간 복잡도: O(n logn)
* -> intervals null check: O(n)
* -> intervals start 값으로 오름차순 정렬. Timsort 사용: O(n logn)
* -> 겹치는 구간 판단 loop: O(n)
*
* 공간 복잡도: O(n)
* -> 정렬된 새로운 미팅 시간 배열 생성: O(n)
* */
fun canAttendMeetings(intervals: List<Interval?>): Boolean {
    if (intervals.isEmpty()) return true
    val sortedByList = intervals.filterNotNull().sortedBy { it.start }
    for (i in 1 until sortedByList.size) {
        if (sortedByList[i - 1].end > sortedByList[i].start) {
            return false
        }
    }
    return true
}
