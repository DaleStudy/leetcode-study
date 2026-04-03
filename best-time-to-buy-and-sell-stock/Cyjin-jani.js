// naive하게 풀면, time limit 초과함
// O(n^2) 풀이가 되기 때문..
const maxProfit_naive = function (prices) {
  let profit = 0;

  for (let i = 0; i < prices.length - 1; i++) {
    const buy = prices[i];
    for (let j = i + 1; j < prices.length; j++) {
      const newProfit = prices[j] - buy;
      if (newProfit > profit) {
        profit = newProfit;
      }
    }
  }

  return profit;
};

// 투포인터 사용하여 풀기
// tc: O(n)
// sc: O(1)
const maxProfit = function (prices) {
  let buyIdx = 0;
  let sellIdx = 1;
  let profit = 0;

  while (sellIdx < prices.length) {
    let buyPrice = prices[buyIdx];
    let sellPrice = prices[sellIdx];

    // 더 낮은 가격에 매수 가능한 날을 찾으면 바로 거기서부터 재탐색
    if (buyPrice > sellPrice) {
      buyIdx = sellIdx;
    } else {
      let newProfit = sellPrice - buyPrice;
      profit = Math.max(profit, newProfit);
    }

    sellIdx++;
  }

  return profit;
};
