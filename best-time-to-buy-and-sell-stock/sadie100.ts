/*
prices를 순회하며 현재 최저값과의 차이를 구해서 최대 profit을 갱신한 뒤 최저값(구매가)를 갱신, 최종값을 리턴한다

시간복잡도 O(N) - N은 prices의 length
*/

function maxProfit(prices: number[]): number {
  let buy
  let result = 0

  for (let price of prices) {
    if (buy === undefined) {
      buy = price
      continue
    }
    result = Math.max(result, price - buy)
    buy = Math.min(price, buy)
  }

  return result
}
