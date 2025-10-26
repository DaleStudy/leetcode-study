/**
 * Definition of Interval:
 * class Interval {
 *     var start: Int = 0
 *     var end: Int = 0
 *     constructor(start: Int, end: Int) {
 *         this.start = start
 *         this.end = end
 *     }
 * }
 */

class Solution {
    /**
     * @param intervals: an array of meeting time intervals
     * @return: the minimum number of conference rooms required
     */
    fun minMeetingRooms(intervals: List<Interval?>): Int {
        // Write your code here
        val points = mutableListOf<List<Int>>()
        intervals.filterNotNull() // T(n) = O(nlogn)
                .forEach {
                    points.add(listOf(it.start, 1,))
                    points.add(listOf(it.end, -1,))
                }
        var ans = 0
        var cnt = 0
        points.sortedBy {it[0]} // T(n) = S(n) = O(n)
                .forEach {
                    cnt += it[1]
                    ans = maxOf(ans, cnt,)
                }
        return ans
    }
}
