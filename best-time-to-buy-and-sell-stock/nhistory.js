/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function (prices) {
  // Initiate left and right pointer (left: buy price / right: sell price)
  // Make profit with initiative value 0
  let l = 0;
  let r = 1;
  let profit = 0;
  // Iterate to check profit = prices[r] - prices[l]
  while (r < prices.length) {
    // If profit is positive, compare profit with previous one
    if (prices[r] > prices[l]) {
      profit = Math.max(profit, prices[r] - prices[l]);
      r++;
    } else {
      // If profit is negative, move forware left and right pointer
      l = r;
      r++;
    }
  }
  return profit;
};

// TC: O(n)
// SC: O(3)

console.log(maxProfit([7, 1, 5, 3, 6, 4])); //5
console.log(maxProfit([7, 6, 4, 3, 1])); //0
