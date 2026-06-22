function longestConsecutive(nums: number[]): number {
  const set = new Set<number>(nums);
  let maxLength = nums.length > 0 ? 1 : 0;
  for(const num of set) {
      if(!set.has(num - 1)) {
          let length = 1;
          let current = num;
          while(set.has(current + 1)) {
              length++;
              current++;
          }
          maxLength = Math.max(maxLength, length);
      }
  }
  return maxLength;
};
