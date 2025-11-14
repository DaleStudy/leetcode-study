/*
시간 복잡도: O(n)
공간 복잡도: O(n)
*.
function twoSum(nums: number[], target: number): number[] {
  const map = new Map<number, number>();

  for (let i = 0; i < nums.length; i++) {
    const num = nums[i];
    const diff = target - num;

    if (map.has(diff)) {
      return [map.get(diff)!, i];
    }

    map.set(num, i);
  }

  return [];
}

/*
이전 풀이
시간 복잡도: O(n²)
공간 복잡도: O(1)
function twoSum(nums: number[], target: number): number[] {
  for (let i = 0; i < nums.length; i++) {
    for (let j = 0; j < nums.length; j++) {
      // 동일한 index일 때는 안됨.
      if (i === j) {
        continue;
      }
      if (nums[i] + nums[j] === target) {
        return [i, j];
      }
    }
    return [];
  }
}

*/
