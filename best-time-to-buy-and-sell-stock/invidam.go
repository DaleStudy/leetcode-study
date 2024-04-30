func maxProfit(prices []int) int {
	purchasePrice := prices[0]
	maxBenefit := 0

	for _, price := range prices {
		purchasePrice = min(purchasePrice, price)
		maxBenefit = max(maxBenefit, price-purchasePrice)
	}
	return maxBenefit
}
