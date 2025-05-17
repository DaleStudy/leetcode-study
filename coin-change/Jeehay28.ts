// Approach 2: Dynamic Programming
// // Time Complexity: O(amout * n), where n is the number of coins
// // Space Complexity: O(amount)

function coinChange(coins: number[], amount: number): number {

    // input: coins = [2, 3, 5], amount = 7

    // initial state dp
    // 0: 0 
    // 1: amount + 1 = 8
    // 2: 8
    // 3: 8
    // 4: 8
    // 5: 8
    // 6: 8
    // 7: 8

    // using coin 2
    // 0: 0 
    // 1: 8
    // 2: 8 -> 8 vs dp[2-2] + 1 = 1 -> 1 
    // 3: 8 -> 8 vs dp[3-2] + 1 = 9 -> 8 
    // 4: 8 -> 8 vs dp[4-2] + 1 = 2 -> 2
    // 5: 8 -> 8 vs dp[5-2] + 1 = 9 -> 8
    // 6: 8 -> 8 vs dp[6-2] + 1 = 3 -> 3
    // 7: 8 -> 8 vs dp[7-2] + 1 = 9 -> 8

    const dp = Array.from({ length: amount + 1 }, () => amount + 1);
    dp[0] = 0

    for (const coin of coins) {
        for (let currentTotal = coin; currentTotal <= amount; currentTotal++) {
            dp[currentTotal] = Math.min(dp[currentTotal - coin] + 1, dp[currentTotal])
        }
    }
  
    return dp[amount] > amount ? -1 : dp[amount]
};


// // Approach 1: BFS Traversal
// // Time Complexity: O(amout * n), where n is the number of coins
// // Space Complexity: O(amount)

// function coinChange(coins: number[], amount: number): number {
//   // queue: [[number of coints, current total]]
//   let queue = [[0, 0]];
//   let visited = new Set();

//   while (queue.length > 0) {
//     const [cnt, total] = queue.shift()!;

//     if (total === amount) {
//       return cnt;
//     }

//     if (visited.has(total)) {
//       continue;
//     }
//     visited.add(total);

//     for (const coin of coins) {
//       if (total + coin <= amount) {
//         queue.push([cnt + 1, total + coin]);
//       }
//     }
//   }

//   return -1;
// }

