const coinChange = function (coins, target) {
  if (target === 0) return 0;

  let level = 0;
  let found = false;

  let queue = [...coins];
  let visit = new Set(coins);

  while (queue.length > 0) {
    level++;

    const queueLength = queue.length;
    for (let i = 0; i < queueLength; i++) {
      const sum = queue.shift();

      if (sum === target) {
        found = true;
        break;
      }

      for (let j = 0; j < coins.length; j++) {
        if (sum + coins[j] > target || visit.has(sum + coins[j])) continue;
        queue.push(sum + coins[j]);
        visit.add(sum + coins[j]);
      }
    }

    if (found) break;
  }

  if (found) return level;
  else return -1;
};

console.log(coinChange([1, 2, 5], 11)); //3
console.log(coinChange([2], 3)); //-1
console.log(coinChange([1], 0)); //0

console.log(coinChange([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 40)); //4

console.log(coinChange([186, 419, 83, 408], 6249)); //20

console.log(
  coinChange([411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422], 9864)
); //24

console.log(coinChange([1, 2], 3)); //2
