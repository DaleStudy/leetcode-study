class Solution {
    func maxArea(_ height: [Int]) -> Int {
        var maxArea = 0
        var startPointIndex = 0
        var endPointIndex = height.count - 1
        while startPointIndex < endPointIndex {
            let minHeight = min(height[startPointIndex], height[endPointIndex])
            let area = minHeight * (endPointIndex - startPointIndex)
            maxArea = max(maxArea, area)
            if height[startPointIndex] < height[endPointIndex] {
                startPointIndex += 1
            } else {
                endPointIndex -= 1
            }
        }
        return maxArea
    }
}

// Time Complexity O(N)
// Space Complexity O(1)
 
