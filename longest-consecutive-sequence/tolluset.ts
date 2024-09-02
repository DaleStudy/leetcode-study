/*
 * TC: O(n)
 * SC: O(n)
 * */
function longestConsecutive(nums: number[]): number {
  const consecutives = [...new Set(nums.sort((a, b) => b - a))];
  const n = consecutives.length;

  if (n === 0) {
    return 0;
  }

  if (n === 1) {
    return 1;
  }

  const bucket = [...Array(n)].map((): Set<number> => new Set());

  let cursor = 0;

  for (let i = 0; i < n; i++) {
    const current = consecutives[i];
    const left = consecutives[i - 1];
    const right = consecutives[i + 1];

    const isLeft = left !== undefined && left - current === 1;
    const isRight = right !== undefined && current - right === 1;

    const isConsecutive = isLeft || isRight;

    if (isConsecutive) {
      bucket[cursor].add(current);

      if (isLeft && !isRight) {
        cursor++;
      }
    } else {
      cursor++;

      continue;
    }
  }

  const total = bucket.reduce(
    (acc, cur) => (acc > cur.size ? acc : cur.size),
    0,
  );

  return total === 0 ? 1 : total;
}

const t1 = longestConsecutive([100, 4, 200, 1, 3, 2]);
console.info("🚀 : tolluset.ts:5: t1=", t1); // 4

const t2 = longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]);
console.info("🚀 : tolluset.ts:8: t2=", t2); // 9

const t3 = longestConsecutive([9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]);
console.info("🚀 : tolluset.ts:40: t3=", t3); // 7

const t4 = longestConsecutive([-6, -1, -1, 9, -8, -6, -6, 4, 4, -3, -8, -1]);
console.info("🚀 : tolluset.ts:59: t4=", t4); //1
