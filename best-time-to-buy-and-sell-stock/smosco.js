/**
 * 핵심 아이디어:
 * 어떤 날에 주식을 팔 때 최대 이익을 얻으려면,
 * 그 날 이전의 최저가에 샀어야 한다.
 * 따라서 배열을 순회하면서 "지금까지의 최저가"만 추적하고,
 * 매 시점마다 (현재가 - 최저가)로 잠재 이익을 계산하면 된다.
 *
 * 시간 복잡도: O(n) - 배열을 한 번만 순회
 * 공간 복잡도: O(1) - 변수 2개만 사용
 */
const maxProfit = (prices) => {
  let minPrice = prices[0];
  let maxProfit = 0;

  for (let i = 1; i < prices.length; i++) {
    const price = prices[i];
    if (price < minPrice) {
      minPrice = price;
    } else if (price - minPrice > maxProfit) {
      maxProfit = price - minPrice;
    }
  }

  return maxProfit;
};
