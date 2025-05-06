class Solution {
    func maxArea(_ height: [Int]) -> Int {
        var start = 0
        var end = height.count - 1
        var result = 0
        
        while start < end {
            let width = end - start
            let waters = width * (min(height[start], height[end]))
            
            result = max(result, waters)
            
            if height[start] > height[end] {
                end  = end - 1
            } else {
                start = start + 1
            }
        }
        
        return result
    }
}
