/**
 * @param {number[]} prices
 * @return {number}
 */
/*
주어진 배열 prices에서 prices[i]는 i번째 날의 주가를 의미한다.

한 번의 거래(1회 매수 + 1회 매도)만 할 수 있으며,
미래의 어떤 날에 매도해야 한다. (즉, 매수일 < 매도일)

목표:
  - 매수 후 매도하여 만들 수 있는 최대 이익을 계산한다.
  - 이익을 낼 수 없다면 0을 반환한다.

입력 형식 :
  - prices: 정수 배열
  - 1 <= prices.length <= 100,000
  - 0 <= prices[i] <= 10,000

출력 형식 :
  - 만들 수 있는 최대 이익 (정수)

예시 :

  Example 1
    입력 : prices = [7,1,5,3,6,4]
    출력 : 5
    설명 :
      - 2번째 날(가격 1)에 매수
      - 5번째 날(가격 6)에 매도
      - 이익 = 6 - 1 = 5

      ※ 매수일보다 앞선 날짜에 매도하는 것은 불가능함.

  Example 2
    입력 : prices = [7,6,4,3,1]
    출력 : 0
    설명 :
      - 어떤 날을 매수해도 이후 가격이 상승하지 않음
      - 이익을 낼 수 없으므로 0 반환
*/
var maxProfit = function(prices) {
    
    let min_value = prices[0];
    let min_value_index = 0;
    let max_value = 0;

    for (let i = 0; i < prices.length; i ++) {
        if(prices[i] < min_value)
        {
            min_value = prices[i];
            min_value_index = i;
        }
    }

    if(min_value_index == (prices.length - 1))
    {
        return 0;
    }

    for (min_value_index; min_value_index < prices.length; min_value_index++)
    {

        if (max_value < prices[min_value_index]) {
            max_value = prices[min_value_index];
        }
    }

    return max_value - min_value;
};

console.log(maxProfit([7,1,5,3,6,4]))
console.log(maxProfit([7,6,4,3,1]))



