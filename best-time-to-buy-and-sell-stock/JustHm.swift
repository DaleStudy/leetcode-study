// time: O(n) space: O(n)
class Solution {
    func maxProfit(_ prices: [Int]) -> Int {
        guard !prices.isEmpty else { return 0 }
        var result = [Int]()
        var current = prices[0]

        for price in prices {
            if current > price {
                current = price
                continue
            }
            result.append(price - current)
        }
        return result.max() ?? 0
    }
}
