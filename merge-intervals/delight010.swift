class Solution {
    // Time O(n log n)
    // Space O(n)
    func merge(_ intervals: [[Int]]) -> [[Int]] {
        if intervals.count <= 1 {
            return intervals
        }
        
        let intervals = intervals.sorted { $0[0] <= $1[0] }
        var answer: [[Int]] = []
        var currentInterval: [Int] = []
        
        for i in 0..<intervals.count {
            if currentInterval.isEmpty {
                currentInterval = intervals[i]
            }
            
            if intervals[i][0] >= currentInterval[0] && intervals[i][0] <= currentInterval[1] {
                currentInterval = [currentInterval[0], max(currentInterval[1], intervals[i][1])]
            } else {
                answer.append(currentInterval)
                currentInterval = intervals[i]
            }
        }
        
        answer.append(currentInterval)
        
        return answer
    }
}
 
