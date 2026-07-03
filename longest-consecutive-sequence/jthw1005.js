const longestConsecutive = (nums) => {
  const set = new Set(nums);
  let longest = 0;

  for (const num of set) {
    if (set.has(num - 1)) continue;
    let current = num;
    let currentStreak = 1;
    while (set.has(current + 1)) {
      current++;
      currentStreak++;
    }
    longest = Math.max(longest, currentStreak);
  }

  return longest;
};
