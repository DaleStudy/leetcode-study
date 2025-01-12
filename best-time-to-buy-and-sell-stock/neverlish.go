// 시간복잡도: O(n)
// 공간복잡도: O(1)

package main

import "testing"

func TestMaxProfit(t *testing.T) {
	prices := []int{7, 1, 5, 3, 6, 4}
	if maxProfit(prices) != 5 {
		t.Error("Test case 0 failed")
	}

	prices = []int{7, 6, 4, 3, 1}
	if maxProfit(prices) != 0 {
		t.Error("Test case 1 failed")
	}
}

func maxProfit(prices []int) int {
	minPrice := prices[0]
	result := 0

	for _, price := range prices {
		profit := price - minPrice
		if profit > result {
			result = profit
		}
		if price < minPrice {
			minPrice = price
		}
	}
	return result
}
