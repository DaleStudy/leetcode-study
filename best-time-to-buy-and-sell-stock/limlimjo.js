/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    
    // 최대 수익
    let maxProfit = 0;
    // prices 배열의 0번째를 최소 가격으로 시작
    let minPrice = prices[0];

    // prices 배열 for문 돌려서 최대 수익 찾기
    for(let i=0; i<prices.length; i++) {
        minPrice = Math.min(minPrice, prices[i]);
        let current = prices[i] - minPrice;
        maxProfit = Math.max(current, maxProfit);
    }
    // 최대 수익 반환
    return maxProfit;

};

// 시간 복잡도: O(n)
// 공간 복잡도: O(1)
