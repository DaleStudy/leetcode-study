/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let left = 0, right = 1;
    let max = 0;
    
    while(right < prices.length) {
        if(prices[right] < prices[left]) {
            left = right;
        } else {
            max = Math.max(max, prices[right] - prices[left]);
        }
        right++;
    }
    return max;
};

// time - O(n) iterate through prices once
// space - O(1) 
