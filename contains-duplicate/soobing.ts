function containsDuplicate(nums: number[]): boolean {
  const checkMap = new Map();
  for(const n of nums) {
      if(checkMap.has(n)) {
          return true;
      } else {
          checkMap.set(n, 1);
      }
  }
  return false;
};
