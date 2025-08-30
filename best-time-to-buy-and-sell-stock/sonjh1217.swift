class Solution {
    func maxProfit(_ prices: [Int]) -> Int {
        var maxProfit = 0
        var minPrice = prices[0]
        
        for i in (1..<prices.count) {
            let profit = prices[i] - minPrice
            maxProfit = max(profit, maxProfit)
            minPrice = min(prices[i], minPrice)
        }
        
        return maxProfit
        
        //시간복잡도 O(n)
        //공간복잡도 O(1)
    }
}

