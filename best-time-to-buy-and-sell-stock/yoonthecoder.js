var maxProfit = function (prices) {
  // set the initial value to Infinity so that it can always return minimum value
  let minPrice = Infinity;
  let maxPrice = 0;
  for (i = 0; i < prices.length; i++) {
    minPrice = Math.min(prices[i], minPrice);
    maxPrice = Math.max(maxPrice, prices[i + 1] - minPrice);
  }
  return maxPrice;
};

// Time complexity: O(n) - Iterating through the array
// Space complexity: O(1)
