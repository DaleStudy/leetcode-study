class Solution {
    func maxProfit(_ prices: [Int]) -> Int {
        var lowPrice: Int = prices[0]
        var maxProfit: Int = 0
        for i in 0..<prices.endIndex {
            lowPrice = min(lowPrice, prices[i])
            maxProfit = max(maxProfit, prices[i] - lowPrice)
        }
        return maxProfit
    }
}
 
