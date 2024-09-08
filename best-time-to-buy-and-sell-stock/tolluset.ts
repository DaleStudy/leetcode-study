/*
 * TC: O(n)
 * SC: O(1)
 * */
function maxProfitV2(prices: number[]): number {
  const n = prices.length;

  let min = Infinity,
    max = 0;

  for (let i = 0; i < n; i++) {
    if (prices[i] < min) {
      min = prices[i];
      continue;
    }

    if (prices[i] - min > max) {
      max = prices[i] - min;
      continue;
    }
  }

  return max;
}

const tc1V2 = maxProfitV2([7, 1, 5, 3, 6, 4]);
console.info("🚀 : tolluset.ts:27: tc1V2=", tc1V2); // 5

const tc2V2 = maxProfitV2([7, 6, 4, 3, 1]);
console.info("🚀 : tolluset.ts:30: tc2V2=", tc2V2); // 0

/*
 * @FAILED: Time Limit Exceeded
 * TC: O(n^2)
 * SC: O(1)
 * */
function maxProfit(prices: number[]): number {
  const n = prices.length;

  let max = 0;

  for (let i = 0; i < n; i++) {
    let currentMax = 0;

    for (let j = i + 1; j < n; j++) {
      if (prices[i] <= prices[j]) {
        const profit = prices[j] - prices[i];

        currentMax = Math.max(currentMax, profit);
      }
    }

    max = Math.max(max, currentMax);
  }

  return max;
}

const tc1 = maxProfit([7, 1, 5, 3, 6, 4]);
console.info("🚀 : tolluset.ts:5: tc1=", tc1); // 5

const tc2 = maxProfit([7, 6, 4, 3, 1]);
console.info("🚀 : tolluset.ts:8: tc2=", tc2); // 0
