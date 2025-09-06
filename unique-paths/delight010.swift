class Solution {
    // Time complexity O(MN)
    // Space complexity O(MN)
    func uniquePaths(_ m: Int, _ n: Int) -> Int {
        let column = Array(repeating: 1, count: n)
        var grid: [[Int]] = Array(repeating: column, count: m)
        for i in 1..<m {
            for j in 1..<n {
                grid[i][j] = grid[i - 1][j] + grid[i][j - 1]
            }
        }
        return grid.last!.last!
    }
}
 
