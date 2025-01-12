/**
 * 최대 이익을 계산하는 함수 
 * @param {number[]} prices 
 * @returns {number}
 * 
 * 시간 복잡도 : O(n) (n: 주식 가격 배열의 길이)
 * 공간 복잡도 : 0(1) (추가 자료구조 X)
 */
function maxProfit(prices: number[]): number {
    let minPrice = 100001; // 지금까지의 최소 가격
    let maxProfit = 0; // 최대 이익

    for (let price of prices) {
        // 최소 가격 갱신
        if (price < minPrice) {
            minPrice = price;
        }

        // 현재 가격에서 최소 가격을 뺀 이익이 최대 이익보다 크다면 갱신
        const potentialProfit = price - minPrice;
        if (potentialProfit > maxProfit) {
            maxProfit = potentialProfit;
        }
    }

    return maxProfit;
}

