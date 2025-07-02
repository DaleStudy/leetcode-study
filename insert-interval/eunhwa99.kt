class Solution {
    fun insert(intervals: Array<IntArray>, newInterval: IntArray): Array<IntArray> {
        val result = mutableListOf<IntArray>()
        var currentStart = newInterval[0]
        var currentEnd = newInterval[1]
        var isAdded = false
        
        // TC: O(n)
        // SC: O(n)
        for(interval in intervals){
            if(isAdded) {
                result.add(interval)
            } else {
                if(interval[1] < currentStart){ // new interval is after the current interval
                    result.add(interval) // just add the interval without any changes
                }
                else if(interval[0] > currentEnd){ // new interval is before the current interval
                    result.add(intArrayOf(currentStart, currentEnd))
                    result.add(interval)
                    isAdded = true
                }
                else{ // intervals overlap, merge them
                    currentStart = minOf(interval[0], currentStart)
                    currentEnd = maxOf(interval[1], currentEnd)
                }
            }
        }
        
        // If new interval wasn't added yet, add it now
        if(!isAdded) {
            result.add(intArrayOf(currentStart, currentEnd))
        }
        
        return result.toTypedArray()
    }
}
