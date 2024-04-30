func maxProfit(prices []int) int {
	maxPriceFrom := make([]int, len(prices)+1)
	for i := len(prices) - 1; i >= 0; i-- {
		maxPriceFrom[i] = max(maxPriceFrom[i+1], prices[i])
	}

	maxPriceDiff := 0
	for i, price := range prices {
		maxPriceDiff = max(maxPriceDiff, maxPriceFrom[i+1]-price)
	}
	return maxPriceDiff
}
