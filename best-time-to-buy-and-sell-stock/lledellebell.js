/**
 * 주어진 주식 가격 배열에서 한 번의 매수와 한 번의 매도를 통해 얻을 수 있는 최대 이익을 계산합니다.
 * 매수는 매도보다 반드시 먼저 이루어져야 합니다.
 *
 * @param {number[]} prices - 각 날짜별 주식 가격을 나타내는 배열
 * @returns {number} 최대 이익 (이익을 낼 수 없는 경우 0 반환)
 *
 * @example
 * maxProfit([7, 1, 5, 3, 6, 4]); // 5 (2일차에 매수하고 5일차에 매도)
 * maxProfit([7, 6, 4, 3, 1]);   // 0 (이익을 낼 수 없음)
 *
 * @description
 * - 시간 복잡도: O(n)
 *   배열을 한 번 순회하며 각 요소에 대해 상수 시간 연산만 수행합니다.
 * - 공간 복잡도: O(1)
 *   추가적인 배열이나 데이터 구조를 사용하지 않고, 두 개의 변수만 사용합니다.
 */
function maxProfit(prices) {
    let min_price = Infinity; // 현재까지의 최소 매수 가격 (초기값은 무한대)
    let max_profit = 0; // 현재까지의 최대 이익 (초기값은 0)

    // 배열을 순회하며 최소 매수 가격과 최대 이익을 계산
    for (let price of prices) {
        if (price < min_price) {
            // 현재 주식 가격이 최소 매수 가격보다 작으면 최소 매수 가격 갱신
            min_price = price;
        } else if (price - min_price > max_profit) {
            // 현재 주식 가격에서 최소 매수 가격을 뺀 값(현재 이익)이 최대 이익보다 크면 최대 이익 갱신
            max_profit = price - min_price;
        }
    }

    return max_profit; // 최대 이익 반환
}
