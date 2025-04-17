function climbStairs(n: number): number {
  // memoization to store the results of the subproblems
  const memo = new Map();

  // if n is 1 or 2, return n
  memo.set(1, 1);
  memo.set(2, 2);

  // recursive function to calculate the number of ways to climb the stairs
  function climb(n: number, memo: Map<number, number>): number {
    let result = memo.get(n);
    if (result) {
      return result;
    } else {
      result = climb(n - 1, memo) + climb(n - 2, memo);
      memo.set(n, result);
      return result;
    }
  }

  return climb(n, memo);
}
