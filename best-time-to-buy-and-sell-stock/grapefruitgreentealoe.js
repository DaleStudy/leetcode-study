var maxProfit = function (prices) {
  let minPrice = Infinity;
  let maxProfit = 0;

  for (let price of prices) {
    // 가장 싼 가격을 갱신
    if (price < minPrice) {
      minPrice = price;
    } else {
      // 최대 이익을 갱신
      maxProfit = Math.max(maxProfit, price - minPrice);
    }
  }

  return maxProfit;
};
