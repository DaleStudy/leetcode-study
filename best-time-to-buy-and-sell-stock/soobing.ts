// 3rd tried
function maxProfit(prices: number[]): number {
  let left = 0;
  let right = 1;
  let max = 0;

  while(left < right && right < prices.length) {
      if(prices[right] - prices[left] > 0) {
          max = Math.max(max, prices[right] - prices[left])
      } else {
          left = right;
      }
      right++;
  }
  return max;
};
