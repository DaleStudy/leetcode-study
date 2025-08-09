function climbStairs(n: number): number {
  type Cache = { [key: number]: number };

  const cache: Cache = {
    2: 2,
    1: 1,
  };

  const fibonacci = (n: number, cache: Cache) => {
    if (n in cache) {
      return cache[n];
    } else {
      cache[n] = fibonacci(n - 2, cache) + fibonacci(n - 1, cache);
      return cache[n];
    }
  };

  return fibonacci(n, cache);
}
