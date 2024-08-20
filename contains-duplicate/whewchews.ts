function containsDuplicate(nums: number[]): boolean {
  const dict: Set<number> = new Set();

  // O(n)
  for (let i = 0; i <= nums.length; i++) {
    const n = nums[i];

    // O(1)
    if (dict.has(n)) return true;
    // O(1)
    dict.add(n);
  }

  return false;
}

// TC: O(N)
// SC: O(N)
