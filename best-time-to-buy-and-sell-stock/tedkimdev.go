// TC: O(n)
// SC: O(1)
func maxProfit(prices []int) int {
	l, r := 0, 1
	max := 0

	for r < len(prices) {
		if prices[l] < prices[r] {
			profit := prices[r] - prices[l]
			if profit > max {
				max = profit
			}
		} else {
			l = r
		}
		r++
	}

	return max
}
