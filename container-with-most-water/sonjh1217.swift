class Solution {
    func maxArea(_ height: [Int]) -> Int {
        var heights = height
        var start = 0
        var end = heights.count - 1
        var maxAmount = 0

        while start < end {
            let startHeight = heights[start]
            let endHeight = heights[end]
            let amount = min(startHeight, endHeight) * (end - start)
            maxAmount = max(amount, maxAmount)

            if startHeight < endHeight {
                start += 1
            } else {
                end -= 1
            }
        }

        return maxAmount

        //시간 O(n)
        //공간 O(1)
    }
}

