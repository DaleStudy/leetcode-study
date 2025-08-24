func maxProfit(prices []int) int {
    ans := 0
    bought := prices[0]
    for i := 1; i != len(prices); i++ {
        ans = max(ans, prices[i] - bought)
        bought = min(bought, prices[i])
    }
    return ans
}
