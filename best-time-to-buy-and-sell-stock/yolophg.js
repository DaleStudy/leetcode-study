var maxProfit = function(prices) {
    let lowBuy = prices[0];
    let profit = 0;
    // loop over the array
    for(let i = 0; i < prices.length; i++) {
        // to set lowBuy to adjust as lower numbers 
        if ( prices[i] < lowBuy ) {
            lowBuy = prices[i];
        } 
        // check the subtract current iteration on array - lowBuy price to calculate current profit
        if ( prices[i] - lowBuy > profit) {
            profit = prices[i] - lowBuy ;
        }
    }
    return profit;
};
