/**
4와 5를 각각 구하면

1+1+1+1
1+1+2
1+2+1
2+1+1
2+2
=> 5

1+1+1+1+1
1+1+1+2
1+1+2+1
1+2+1+1
2+1+1+1
1+2+2
2+1+2
2+2+1
=> 8

왜 피보나치 수열 같을까? 일단 그렇게 값을 계산해보자.

시간 복잡도: O(n)
공간 복잡도: O(n)

근데 왜 피보나치인지는 생각해보고 업데이트 하기..
*/

function climbStairs(n: number): number {
  if (n === 1) {
    return 1;
  }

  if (n === 2) {
    return 2;
  }

  const results = [1, 2];
  for (let i = 2; i < n; i++) {
    results.push(results[i - 2] + results[i - 1]);
  }

  return results.pop() as number;
}
