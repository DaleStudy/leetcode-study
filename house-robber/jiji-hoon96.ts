function rob(nums: number[]): number {
  let take = 0;
  let skip = 0;

  for (const num of nums) {
    const nextTake = skip + num;
    const nextSkip = Math.max(take, skip);

    take = nextTake;
    skip = nextSkip;
  }

  return Math.max(take, skip);
}

rob([1, 2, 3, 1]); // 4
rob([2, 7, 9, 3, 1]); // 12
