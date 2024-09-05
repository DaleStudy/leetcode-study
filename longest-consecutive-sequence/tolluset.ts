/*
 * TC: O(n)
 * SC: O(n)
 * */
function longestConsecutive(nums: number[]): number {
  const n = nums.length;

  if (n <= 1) {
    return n;
  }

  const numsSet = new Set(nums);
  let longestLen = 0;

  for (let i = 0; i < n; i++) {
    let current = nums[i];

    if (!numsSet.has(current - 1)) {
      let currentLen = 1;

      while (numsSet.has(current + 1)) {
        current++;
        currentLen++;
      }

      longestLen = Math.max(longestLen, currentLen);
    }
  }
  return longestLen;
}

const t1 = longestConsecutive([100, 4, 200, 1, 3, 2]);
console.info("🚀 : tolluset.ts:5: t1=", t1); // 4

const t2 = longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]);
console.info("🚀 : tolluset.ts:8: t2=", t2); // 9

const t3 = longestConsecutive([9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]);
console.info("🚀 : tolluset.ts:40: t3=", t3); // 7

const t4 = longestConsecutive([-6, -1, -1, 9, -8, -6, -6, 4, 4, -3, -8, -1]);
console.info("🚀 : tolluset.ts:59: t4=", t4); // 1
