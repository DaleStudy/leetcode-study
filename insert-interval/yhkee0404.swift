class Solution {
    func insert(_ intervals: [[Int]], _ newInterval: [Int]) -> [[Int]] {
        var ans: [[Int]] = []
        var i = 0
        while i != intervals.count && intervals[i][1] < newInterval[0] {
            ans.append(intervals[i])
            i += 1
        }
        var newInterval = newInterval
        if i != intervals.count && intervals[i][0] <= newInterval[0] {
            newInterval[0] = intervals[i][0]
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        }
        while i != intervals.count && intervals[i][1] <= newInterval[1] {
            i += 1
        }
        if i != intervals.count && intervals[i][0] <= newInterval[1] {
            newInterval[1] = intervals[i][1]
            i += 1
        }
        ans.append(newInterval)
        while i != intervals.count {
            ans.append(intervals[i])
            i += 1
        }
        return ans
    }
}
