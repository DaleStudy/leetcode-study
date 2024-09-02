/*
 * TC: O(n)
 * SC: O(1)
 * */
function missingNumber(nums: number[]): number {
  const n = nums.length;

  const sum = (n * (n + 1)) / 2;
  const actualSum = nums.reduce((acc, curr) => acc + curr, 0);

  if (sum === actualSum) {
    return 0;
  }

  return sum - actualSum;
}

const t1 = missingNumber([3, 0, 1]);
console.info("🚀 : tolluset.ts:3: t1=", t1); // 2

const t2 = missingNumber([0, 1]);
console.info("🚀 : tolluset.ts:6: t2=", t2); // 2

const t3 = missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]);
console.info("🚀 : tolluset.ts:9: t3=", t3); // 8
