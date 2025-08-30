/**
 * 문제 유형
 * - Array
 *
 * 문제 설명
 * - 주식을 가장 싸게 사서 비싸게 팔수 있는 경우 찾기
 *
 * 아이디어
 * 1) 최소값을 찾고 그 이후의 값 중 최대값을 찾는다.
 *
 */
function maxProfit(prices: number[]): number {
  let min = prices[0];
  let maxProfit = 0;

  for (let i = 1; i < prices.length; i++) {
    min = Math.min(min, prices[i]);
    maxProfit = Math.max(prices[i] - min, maxProfit);
  }
  return maxProfit;
}
