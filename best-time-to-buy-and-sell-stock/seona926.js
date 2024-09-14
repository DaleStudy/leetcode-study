function maxProfit(prices) {
    let minPrice = Infinity;  // 최소 가격을 무한대로 초기화
    let maxProfit = 0;        // 최대 이익은 0으로 시작

    for (let i = 0; i < prices.length; i++) {
        if (prices[i] < minPrice) {
            // 더 작은 가격을 발견하면 그 가격을 최소 가격으로 업데이트
            minPrice = prices[i];
        } else {
            // 현재 가격에서 최소 가격을 뺀 값을 계산하여 최대 이익을 업데이트
            maxProfit = Math.max(maxProfit, prices[i] - minPrice);
        }
    }

    return maxProfit;
}

/*
    1. 시간복잡도: O(n)
        - 배열을 한 번 순회
    2. 공간복잡도: O(1)
        - 상수 공간 사용
*/