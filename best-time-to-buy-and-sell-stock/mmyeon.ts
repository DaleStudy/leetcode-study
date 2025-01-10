/**
 *
 * 접근 방법 :
 *  - max profit을 구하는 문제로 O(n)으로 풀기
 *  - 현재 가격에서 가장 낮은 가격을 뺀 값을 max profit으로 설정
 *
 * 시간복잡도 : O(n)
 *  - n은 prices 길이, 요소 1회 순회하니까 O(n)
 *
 * 공간복잡도 : O(1)
 *  - 변수 2개 사용하니까 O(1)
 */

function maxProfit(prices: number[]): number {
  let minPrice = prices[0],
    maxProfit = 0;

  for (const price of prices) {
    minPrice = Math.min(price, minPrice);
    maxProfit = Math.max(maxProfit, price - minPrice);
  }

  return maxProfit;
}
