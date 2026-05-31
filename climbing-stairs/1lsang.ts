// n번째 칸 까지 오르기 위해서는 n-1번째 칸에서 1칸을 오르거나 n-2번째 칸에서 2칸을 오르면 됨.

/* 
최초에 생각한 방법은 재귀 구현 But 재귀 구현시에는 O(2^n)으로 시간복잡도가 너무 커서 Time Limit에 걸림.

function climbStairs(n: number): number {
  if (n === 1) return 1; // 1칸을 오르는 방법은 1개
  if (n === 2) return 2; // 2칸을 오르는 방법은 1+1/2 2개
  return climbStairs(n-1) + climbStairs(n-2);
};
*/

function climbStairs(n: number): number {
  const arr: number[] = [1, 2];
  for (let i = 2; i < n; i++) {
    arr.push(arr[i-1] + arr[i-2]);
  }
  return arr[n-1];
};
