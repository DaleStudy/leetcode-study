function twoSum(nums: number[], target: number): number[] {
    const hashTable = nums.reduce((acc, v, i) => {
        acc[v] = i;
        return acc;
    }, {});



  for (const index1 of nums.keys()) {
    const v = nums[index1];
    const remain = target - v;
    
    if(hashTable.hasOwnProperty(remain) && index1 !== hashTable[remain]) {
        return [index1, hashTable[remain]];
    }
  }

  return []
};