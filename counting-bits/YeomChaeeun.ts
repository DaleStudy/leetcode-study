/**
 * 이진수에서 1의 개수 세기 알고리즘
 * 알고리즘 복잡도
 * - 시간 복잡도: O(n * log n)
 * - 공간 복잡도: O(n)
 */
function countBits(n: number): number[] {
  const result: number[] = [];

  // 비트 연산을 이용해 1의 개수를 세는 함수 - O(log n)
  function countOnes(num: number): number {
    let count = 0;
    while (num > 0) {
      num &= (num - 1);  // 가장 오른쪽의 1 비트를 제거
      count++;
    }
    return count;
  }

  for (let i = 0; i <= n; i++) {
    result.push(countOnes(i));
  }
  
  return result;
}

