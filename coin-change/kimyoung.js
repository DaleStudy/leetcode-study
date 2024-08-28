var coinChange = function (coins, amount) {
    // create a dp array that stores the minimum amount of coins used for each amount leading up to the target amount
    // fill with array with amount + 1 as a default 
    const dp = [0, ...new Array(amount).fill(amount + 1)];

    // loop through the coins 
    for (const coin of coins) {
        // for each amount, assess how the current coin can modify the existing value within the dp array by comparing the min value
        for (let i = 1; i <= amount; i++) {
            // only works if coin is less than or equal to the assessing amount
            if (coin <= i) {
                // min comparison 
                dp[i] = Math.min(dp[i], dp[i - coin] + 1);
            }
        }
    }
    // check target amount in dp array to see if it's the default value
    // if it's default value, it means coin combination cannot lead up to target amount
    // if it's not default value, that is the minimum required coin change to lead up to target amount
    return dp[amount] === amount + 1 ? -1 : dp[amount];
};

// time - O(a * c) loops through amount * loops through coin
// space - O(a) depends on the size of amount