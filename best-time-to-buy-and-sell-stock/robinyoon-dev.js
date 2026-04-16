/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function (prices) {

    let minPrice = prices[0];
    let maxProfit = 0;

    for (let i = 1; i < prices.length; i++) {
        let currentPrice = prices[i];

        if (currentPrice < minPrice) {
            minPrice = currentPrice;
        } else{
            let profit = currentPrice - minPrice;
            if(profit > maxProfit){
                maxProfit = profit;
            }
        }
    }

    return maxProfit;
};

// -----아래는 이전에 작성한 답안입니다.
// /**
//  * @param {number[]} prices
//  * @return {number}
//  */
// var maxProfit = function(prices) {
 
//     // NOTE: 해설 보고 쓴 코드입니다.
//     // i 번째 날에 prices[i]의 가격으로 주식을 팔아서 가장 큰 이익을 내려면 주식을 언제 샀어야 했을까?
//     // 정답은 바로 i 번째 날이 오기 전에 주식이 가장 쌌던 날 입니다!

//     let maxProfit = 0;
//     let minPrice = prices[0];

//     for(const price of prices){
//         const profit = price - minPrice
//         maxProfit = Math.max(maxProfit, profit);
//         minPrice = Math.min(price, minPrice);
//     }

//     return maxProfit;

// };

