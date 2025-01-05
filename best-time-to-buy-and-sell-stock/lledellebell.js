/*
Time complexity: O(n)
Space complexity: O(1)

문제 설명:
- 주어진 배열 `prices`에서, i <= j인 두 인덱스 i, j에 대해 prices[j] - prices[i]를 최대화해야 합니다.
- 즉, 한 번의 매수와 한 번의 매도를 통해 얻을 수 있는 최대 이익을 계산합니다.
- 매수는 매도보다 반드시 먼저 이루어져야 합니다.

알고리즘 설명:
1. 배열을 왼쪽에서 오른쪽으로 한 번 순회합니다.
2. 현재 주식 가격이 `min_price`보다 작으면, `min_price`를 갱신합니다.
   - `min_price`는 현재까지의 최소 매수 가격을 의미합니다.
3. 현재 주식 가격에서 `min_price`를 뺀 값(현재 이익)이 `max_profit`보다 크면, `max_profit`을 갱신합니다.
   - `max_profit`은 현재까지의 최대 이익을 의미합니다.
4. 배열 순회가 끝난 후, `max_profit`을 반환합니다.

시간 복잡도:
- 배열을 한 번만 순회하므로 O(n)입니다.

공간 복잡도:
- 추가적인 배열이나 데이터 구조를 사용하지 않고, 두 개의 변수(`min_price`, `max_profit`)만 사용하므로 O(1)입니다.
*/

function maxProfit(prices) {
    let min_price = Infinity; // 초기 최소값을 무한대로 설정 (어떤 값과 비교해도 갱신되도록 설정)
    let max_profit = 0; // 초기 최대 이익은 0 (이익이 없을 경우에도 0을 반환해야 함)

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