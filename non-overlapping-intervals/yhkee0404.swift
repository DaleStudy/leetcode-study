class Solution {
    func eraseOverlapIntervals(_ intervals: [[Int]]) -> Int {
        let intervals = intervals.sorted() { $0[1] < $1[1] } // T(n) = S(n) = O(nlogn)
        var ans = 0
        var end = -50_000
        for se in intervals {
            if se[0] < end {
                ans += 1
                continue
            }
            end = se[1]
        }
        return ans
    }
}
