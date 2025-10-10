class Solution {
    /// 구간을 다루는데, 겹치지 않게 최대/최소로 뽑는 문제 -> 끝점 기준 정렬 + 그리디
    /// 가장 빨리 끝나는 것들을 선택해야 최대한 많이 선택할 수 있음
    /// 끝점 기준 오름차순 정렬 nlogn
    /// 순차적으로 돌면서 겹치면 제거(앞 것들보다 끝점이 더 뒤라서, 시작만 확인하면 됨)
    /// O(nlogn) time / O(n) space
    func eraseOverlapIntervals(_ intervals: [[Int]]) -> Int {
        let intervals = intervals.sorted { $0[1] < $1[1] }
        var end = intervals[0][1]
        var removal = 0
        
        for i in 1..<intervals.count {
            let isOverlapping = intervals[i][0] < end
            if isOverlapping {
                removal += 1
            } else {
                end = intervals[i][1]
            }
        }
        
        return removal
    }
}
