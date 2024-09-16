/*
 * 아이디어
 * 수익을 얻기 위해서는 index보다 뒤에 오는 값 중에 현재 값보다 큰 값이 있어야 한다
 * 차이가 가장 큰 두 값을 찾으면 되는데, 그 값의 순서가 작은값 다음 큰 값 순이어야 한다
 * 가격의 차이를 어떻게 구할 수 있을까?
 * for문을 두번 돌면서 값의 차이를 저장해둔다.(순서가 일치해야함)
 * 값의 차이 중 가장 큰 값을 리턴한다.
 * 리턴할 값이 없으면 0을 리턴한다.
 * ====> 이 방법으로 풀었더니 타임초과가 나왔다.
 * 어떻게 시간복잡도를 줄일 수 있을까?
 * for문을 두번돌면 O(n^2)이 드니 for문을 한번만 돌게 하면 좋을 것 같다.
 * for문을 돌면서 가장 작은 구매가, 최대 이익 두가지 변수를 업데이트 하자
 * ===> 연습삼아 투포인터로도 풀어보자
 */

function maxProfit1(prices: number[]): number {
  let profit = 0;

  for (let i = 0; i <= prices.length - 2; i++) {
    const x = prices[i];
    for (let j = i + 1; j <= prices.length - 1; j++) {
      const y = prices[j];
      const diff = y - x;
      if (x < y && profit < diff) {
        profit = diff;
      }
    }
  }

  return profit;
}
// TC: O(n^2)
// SC: O(1)

function maxProfit2(prices: number[]): number {
  let buyPrice = prices[0];
  let profit = 0;

  for (let i = 0; i <= prices.length - 1; i++) {
    const todayPrice = prices[i];
    const diff = todayPrice - buyPrice;

    if (todayPrice <= buyPrice) {
      buyPrice = todayPrice;
    } else {
      if (profit < diff) {
        profit = todayPrice - buyPrice;
      }
    }
  }

  return profit;
}
// TC: O(n)
// SC: O(1)

function maxProfit3(prices: number[]): number {
  let left = 0;
  let right = 1;
  let maxProfit = 0;

  while (right <= prices.length - 1) {
    if (prices[left] > prices[right]) {
      left = right;
    } else {
      const profit = prices[right] - prices[left];
      maxProfit = Math.max(profit, maxProfit);
    }

    right++;
  }

  return maxProfit;
}
// TC: O(n)
// SC: O(1)
