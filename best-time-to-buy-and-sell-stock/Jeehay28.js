/**
 * @param {number[]} prices
 * @return {number}
 */

// TC : O(n)
// SC : O(1)

var maxProfit = function (prices) {
  if (prices.length === 1) {
    return 0;
  }

  // Two variables (profitMax and priceMin) are used to store the maximum profit and minimum price seen, which require O(1) space.
  let profitMax = 0;
  let priceMin = prices[0];

  for (const price of prices) {
    const profit = price - priceMin;
    profitMax = Math.max(profit, profitMax);
    priceMin = Math.min(price, priceMin);
  }

  return profitMax;
};

// Why Constants Are Ignored in Big-O
// In Big-O notation, O(2) is simplified to O(1) because constants are irrelevant in asymptotic analysis.
// Big-O focuses on how resource usage scales with input size, not fixed values.

// Using 2 variables: O(1)
// Using 10 variables: O(1)
// Using 100 variables: O(1)

// What Space Complexity Looks Like for Larger Growth
// O(n): Memory grows linearly with the input size (e.g., storing an array of n elements).
// O(n^2): Memory grows quadratically (e.g., a 2D matrix with n*n elements).
// 𝑂(log 𝑛): Memory grows logarithmically (e.g., recursive calls in binary search).
// O(1): Fixed memory usage, regardless of input size (e.g., using a fixed number of variables).


