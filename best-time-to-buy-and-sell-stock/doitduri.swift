class Solution {
    func maxProfit(_ prices: [Int]) -> Int {
        guard var anchor = prices.first, prices.count > 1 else {
            return 0
        }
        
        var result = 0
        for price in prices {
            if price < anchor {
                anchor = price
            } else if price - anchor > result {
                result = price - anchor
            }
        }
        
        return result
    }
}
