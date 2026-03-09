// 1트
// tc: O(n)
// sc: O(n)
const climbStairs_before = function (n) {
  // 1걸음 혹은 2걸음만 이동 가능하니까 전 step까지의 결과 + 전전 step까지의 결과
  // D(n-1) + D(n-2)
  const data = [0, 1, 2];

  for (let i = 1; i <= n; i++) {
    if (!data[i]) {
      data[i] = data[i - 1] + data[i - 2];
    }
  }

  return data[n];

  // 이렇게 풀면 sc가 O(n)...
  // 더 나은 방법을 고민하는 것이 필요..
};

// 2트
// tc: O(n)
// sc: O(1)
const climbStairs = function (n) {
  if (n < 3) return n;

  let d1 = 1;
  let d2 = 2;

  for (let i = 3; i <= n; i++) {
    let sum = d1 + d2;
    d1 = d2;
    d2 = sum;
  }

  return d2;
};
