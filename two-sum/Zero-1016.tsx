/**
 * Time Complexity: O(n)
 * Space Complexity: O(n)
 * 배열에서 두 숫자를 더해서 target이 되는 인덱스를 반환한다.
 */
function twoSum(nums: number[], target: number): number[] {
  const seenNumbers = new Map<number, number>();

  for (let i = 0; i < nums.length; i++) {
    const currentNumber = nums[i];
    const targetNumber = target - currentNumber;

    if (seenNumbers.has(targetNumber)) {
      return [seenNumbers.get(targetNumber)!, i];
    }

    seenNumbers.set(currentNumber, i);
  }

  return [];
}
