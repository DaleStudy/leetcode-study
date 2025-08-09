function topKFrequent(nums: number[], k: number): number[] {
  nums.sort((a, b) => a - b);

  const countMap = new Map<number, number>();

  let pointer = 0;
  while (pointer < nums.length) {
    const currentNumber = nums[pointer];
    let count = 0;

    while (nums[pointer] === currentNumber) {
      pointer++;
      count++;
    }

    countMap.set(currentNumber, count);
  }

  const result = Array.from(countMap)
    .sort((a, b) => b[1] - a[1])
    .slice(0, k)
    .map((value) => value[0]);

  return result;
}
