// https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

package hello

func maxProfit(prices []int) int {
	min := prices[0]
	maxProfit := 0

	for i := 1; i < len(prices); i++ {
		if prices[i] < min {
			min = prices[i]
		}
		if (prices[i] - min) > maxProfit {
			maxProfit = prices[i] - min
		}
	}

	return maxProfit
}
