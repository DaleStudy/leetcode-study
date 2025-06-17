class Solution {
    // TC: O(n log n) - intervals를 정렬하는데 O(n log n)
    // SC: O(1) - 추가적인 공간을 사용하지 않음
    fun eraseOverlapIntervals(intervals: Array<IntArray>): Int {
        intervals.sortBy { it[1] } // intervals를 끝나는 시간 기준으로 정렬

        var prevEnd = intervals[0][1]
        var count = 0
        for (i in 1 until intervals.size) {
            val curStart = intervals[i][0]
            if (curStart < prevEnd) { // 두 구간이 겹친다.
                count++
            } else {
                prevEnd = intervals[i][1] // 겹치지 않으면 prevEnd를 갱신
            }

        }
        return count
    }
}
