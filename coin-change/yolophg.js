// Time Complexity: O(amount * coins.length)
// Space Complexity: O(amount)

var coinChange = function (coins, amount) {
  // if the amount is 0, no coins are needed
  if (amount === 0) return 0;

  // a queue to hold the current amount and coins used to reach that amount
  let queue = [{ amount: 0, steps: 0 }];

  // a set to keep track of visited amounts to avoid revisiting them
  let visited = new Set();
  visited.add(0);

  // start the BFS loop
  while (queue.length > 0) {
    // dequeue the first element
    let { amount: currentAmount, steps } = queue.shift();

    // iterate through each coin
    for (let coin of coins) {
      // calculate the new amount by adding the coin to the current amount
      let newAmount = currentAmount + coin;

      // if the new amount equals the target amount, return the number of steps plus one
      if (newAmount === amount) {
        return steps + 1;
      }

      // if the new amount is less than the target amount and hasn't been visited, enqueue it
      if (newAmount < amount && !visited.has(newAmount)) {
        queue.push({ amount: newAmount, steps: steps + 1 });
        visited.add(newAmount);
      }
    }
  }

  // if the loop completes without finding the target amount, return -1
  return -1;
};
