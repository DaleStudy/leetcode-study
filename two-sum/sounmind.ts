function twoSum(nums: number[], target: number): number[] {
  // Pair each element with its index
  const numsWithIndex = nums.map((value, index) => ({ value, index }));

  // Sort the array based on the values
  numsWithIndex.sort((a, b) => a.value - b.value);

  let left = 0;
  let right = numsWithIndex.length - 1;

  while (left < right) {
    const sum = numsWithIndex[left].value + numsWithIndex[right].value;

    if (sum === target) {
      return [numsWithIndex[left].index, numsWithIndex[right].index];
    } else if (sum < target) {
      left++;
    } else {
      right--;
    }
  }

  return []; // In case there is no solution
}
