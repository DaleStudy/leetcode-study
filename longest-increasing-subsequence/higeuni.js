/**
 * @param {number[]} nums
 * @return {number}
 * 
 * complexity
 * time: O(nlogn) : lower_bound : O(logn), for문 : O(n)
 * space: O(n)
 */
var lengthOfLIS = function(nums) {
  const lower_bound = (arr, value) => {
      let ret = -1;
      let l = 0;
      let r = arr.length - 1;

      while(l <= r) {
          const mid = Math.floor((l + r) / 2);
          if(arr[mid] >= value) {
              ret = mid;
              r = mid - 1;
          } else {
              l = mid + 1;
          }
      }

      return ret;
  }

  let sequence = [];

  for(let i=0; i<nums.length; i++) {
      const ret = lower_bound(sequence, nums[i])
      if(ret === -1) {
          sequence.push(nums[i]);
      } else {
          sequence[ret] = nums[i]
      }
  }

  return sequence.length;
};

