function twoSum(nums: number[], target: number): number[] {
  const map = new Map<number, number[]>();
  for(let i = 0; i < nums.length; i++) {
      const current = map.get(nums[i]);
      if(current) {
          current.push(i);
      } else {
          map.set(nums[i], [i]);
      }
  }

  nums.sort((a, b) => a - b);
  let left = 0;
  let right = nums.length - 1;

  while(left < right) {
      if(nums[left] + nums[right] === target) {
          return [map.get(nums[left])?.pop() ?? 0, map.get(nums[right])?.pop() ?? 0];
      }

      if(nums[left] + nums[right] > target) {
          right--;
      } else {
          left++;
      }
  }

  return [];
};