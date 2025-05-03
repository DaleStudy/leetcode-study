function maxProfit(prices: number[]): number {
  if (prices.length <= 1) return 0;
  
  let minPrice = prices[0];
  let maxProfit = 0;
  
  for (let i = 1; i < prices.length; i++) {
      // 현재 가격이 최소가보다 낮으면 최소가 업데이트
      if (prices[i] < minPrice) {
          minPrice = prices[i];
      } 
      // 현재 가격으로 팔았을 때의 이익 계산
      else {
          const currentProfit = prices[i] - minPrice;
          // 최대 이익 업데이트
          if (currentProfit > maxProfit) {
              maxProfit = currentProfit;
          }
      }
  }
  
  return maxProfit;
}