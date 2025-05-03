/**
 * 시간 복잡도: O(n) - 배열을 한 번만 순회함
 * 공간 복잡도: O(1) - 추가 배열 없이 변수만 사용하므로 입력 크기와 무관한 상수 공간
 */
/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function (prices) {
  let minPrice = prices[0]; // 지금까지 본 가장 낮은 가격
  let maxProfit = 0; // 최대 이익
  for (let i = 1; i < prices.length; i++) {
    if (prices[i] > minPrice) {
      // 현재 가격이 minPrice보다 큰 경우에 이익 갱신
      maxProfit = Math.max(maxProfit, prices[i] - minPrice);
    } else {
      // 그렇지 않다면 최소 가격 갱신
      minPrice = prices[i];
    }
  }
  return maxProfit;
};
