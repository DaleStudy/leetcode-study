function twoSum(nums: number[], target: number): number[] {
    // hasTable을 생성
    const hashTable = nums.reduce((acc, v, i) => {
        acc[v] = i;
        return acc;
    }, {});



    for (const index of nums.keys()) {
    const v = nums[index];
    const remain = target - v;
    
    // target을 만들기 위해 필요한 값을 hashTable에서 조회하고 있으면 결과로 리턴
    if(hashTable.hasOwnProperty(remain) && index !== hashTable[remain]) {
        return [index, hashTable[remain]];
    }
  }

  return []
};
