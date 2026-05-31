function combinationSum(candidates: number[], target: number): number[][] {
  // arr: index까지 갈 수 있는 combinationSum
  const arr:number[][][] = Array.from({ length: target + 1 }, () => [] as number[][]); 
  // 0을 만들 수 있는 방법은 숫자가 없는 것
  arr[0].push([] as number[]);
  
  for (const candidate of candidates) {
    for (let n = candidate; n <= target; n++) {
      for (const combination of arr[n-candidate]) {
        arr[n].push([...combination, candidate]);
      }
    }
  }
  console.log(arr);
  return arr[target];
};
