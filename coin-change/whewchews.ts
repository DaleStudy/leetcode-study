function coinChange(coins: number[], amount: number): number {
  /* # Solution 1: BFS
   *  최소 경로를 찾는 문제 => BFS
   * 현재까지 사용한 동전의 개수와 현재까지 사용한 동전의 합을 queue에 넣는다.
   * visited: 중복 방문을 방지하기 위한 set
   * 누적액이 amount와 같아지면 count를 return
   * visited에 누적액이 있으면 continue
   * coins를 순회하면서 누적액에 동전을 더한 값이 amount보다 작으면 queue에 넣는다.
   * queue가 빌때까지 반복
   * 큐가 비어있고 amount를 만들수 없으면 -1을 return
   */
  const queue = [[0, 0]]; // [number of coins, accumulated amount]
  const visited = new Set();

  while (queue.length > 0) {
    const [count, total] = queue.shift();
    if (total === amount) {
      return count;
    }
    if (visited.has(total)) {
      continue;
    }
    visited.add(total);
    for (const coin of coins) {
      if (total + coin <= amount) {
        queue.push([count + 1, total + coin]);
      }
    }
  }
  return -1;
}
// TC: 각 금액(amount)마다 동전(coins)을 순회하므로 O(N^2*M) N: amount, M: coins.length
// SC: O(N) N: amount
