// [191] Number of 1 Bits

/**
 * [Idea]
 * 숫자를 2진수로 변환해서 (toString) 1인 비트를 직접 세줬다.
 *
 * [Time Complexity]
 * toString 내부에서 진법 변환을 수행하는 과정에서 나눗셈을 반복적으로 수행하기 때문에 시간복잡도는 O(log n)
 *
 * [Space Complexity]
 * 변환된 수의 자릿수만큼의 공간이 필요하므로 공간복잡도는 O(log n)
 */
function hammingWeight(n: number): number {
  const binary = n.toString(2);
  return [...binary].reduce(
    (count, bit) => (bit === "1" ? count + 1 : count),
    0
  );
}
