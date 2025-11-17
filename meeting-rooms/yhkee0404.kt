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
     * @return: if a person could attend all meetings
     */
    fun canAttendMeetings(intervals: List<Interval?>): Boolean {
        // Write your code here
        val sorted = intervals.filterNotNull() // T(n) = O(nlogn)
            	.sortedBy {it!!.end}
        return (1 until intervals.size).all {sorted[it].start >= sorted[it - 1].end}
    }
}
