/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function (prices) {
  // 초기 값
  let buy = prices[0];
  // 차액
  let diff = 0;
  
  for (let i = 1; i < prices.length; i++) {
      // 구매가보다 현재가격이 더 싸면 구매가로 변경
      if (buy > prices[i]) { 
          buy = prices[i];
      }
      // 차액 계산, 누가더 큰지 비교
      diff = Math.max(diff, (prices[i] - buy));

  }
  return diff
};
