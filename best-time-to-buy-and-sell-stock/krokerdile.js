var maxProfit = function(prices) {
    let minPrice = Infinity;
    let maxProfit = 0;

    for (let price of prices) {
        if (price < minPrice) {
            minPrice = price; // 더 싼 가격이 나타나면 갱신
        } else {
            maxProfit = Math.max(maxProfit, price - minPrice); // 이익 갱신
        }
    }

    return maxProfit;
};
