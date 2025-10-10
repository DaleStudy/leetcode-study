class Solution {
    // Time O(n log n)
    // Space O(n)
    func eraseOverlapIntervals(_ intervals: [[Int]]) -> Int {
        if intervals.count < 2 { return 0 }
        
        var answer = 0
        let intervals = intervals.sorted { $0[1] < $1[1] }
        var currentInterval = intervals[0]
        
        for i in 1..<intervals.count {
            if currentInterval[1] <= intervals[i][0] {
                currentInterval = intervals[i]
            } else {
                answer += 1
            }
        }
        
        return answer
    }
}
 
