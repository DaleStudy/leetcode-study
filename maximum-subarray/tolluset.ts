/*
 * TC: O(n)
 * SC: O(1)
 * */
function maxProduct(nums: number[]): number {
  const n = nums.length;

  if (n === 1) {
    return nums[0];
  }

  let max = 0,
    min = 0,
    res = 0;

  for (let i = 0; i < n; i++) {
    const cur = nums[i];

    if (cur < 0) {
      [max, min] = [min, max];
    }

    max = Math.max(cur, max * cur);
    min = Math.min(cur, min * cur);

    res = Math.max(res, max);
  }

  return res;
}

const t1 = maxProduct([2, 3, -2, 4]);
console.info("🚀 : tolluset.ts:3: t1=", t1); // 6

const t2 = maxProduct([-2, 0, -1]);
console.info("🚀 : tolluset.ts:6: t2=", t2); // 0

const t3 = maxProduct([-2]);
console.info("🚀 : tolluset.ts:34: t3=", t3); // -2
