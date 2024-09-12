class SolutionJaeJeong {

  public int maxProfit(int[] prices) {
    // 주어진 가격 배열이 주어지고 prices[i]는 i번째 날의 주어진 주식 가격
    // 한 주식을 매수할 단일 날짜를 선택하고, 매도할 미래의 다른 날짜를 선택해 수익을 극대화
    // 이 거래에서 얻을 수 있는 최대 수익을 반환해라, 수익을 얻을 수 없으면 0을 반환해라
    // 싸게 매수해서 비싸게 매도해라

    // 3번째 풀이
    // 최대 이익: 현재 가격 - 이전 가격 중 최저 가격
    // 시간복잡도: O(N), 공간복잡도: O(1)
    int minPrice = prices[0];
    int maxProfit = 0;
    for (int i = 1; i < prices.length; i++) {
      if (prices[i - 1] < minPrice) {
        minPrice = prices[i - 1];
      }

      var profit = prices[i] - minPrice;
      if (profit > maxProfit) {
        maxProfit = profit;
      }
    }

    return maxProfit;
  }
}