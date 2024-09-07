//time-complexity : O(n)
//space-complexity : O(n)

const longestConsecutive = function (nums) {
  let longest = 0;
  const set = new Set(nums);

  while (set.size > 0) {
    let count = 0;
    const originalSeed = set.values().next().value; //set의 첫 번째 원소 get

    seed = originalSeed;

    while (set.has(seed)) {
      set.delete(seed);
      count++;
      seed += 1;
    }

    seed = originalSeed - 1;

    while (set.has(seed)) {
      set.delete(seed);
      count++;
      seed -= 1;
    }

    if (count > longest) longest = count;
  }

  return longest;
};
