/*
 * TC: O(n^2)
 * SC: O(n)
 * */
function threeSum(nums: number[]): number[][] {
  const n = nums.length;
  const res: number[][] = [];

  nums.sort((a, b) => a - b);

  for (let i = 0; i < n - 2; i++) {
    if (i > 0 && nums[i] === nums[i - 1]) {
      continue;
    }

    let left = i + 1,
      right = n - 1;

    while (left < right) {
      const sum = nums[i] + nums[left] + nums[right];

      if (sum === 0) {
        res.push([nums[i], nums[left], nums[right]]);

        while (nums[left] === nums[left + 1]) {
          left++;
        }

        while (nums[right] === nums[right - 1]) {
          right++;
        }

        left++;
        right--;

        continue;
      }

      if (sum < 0) {
        left++;

        continue;
      }

      right--;
    }
  }

  return res;
}

const tc1 = threeSum([-1, 0, 1, 2, -1, -4]); // [[-1,-1,2],[-1,0,1]]
console.info("🚀 : tolluset.ts:39: tc1=", tc1);

const tc2 = threeSum([0, 0, 0]); // [[0,0,0]]
console.info("🚀 : tolluset.ts:42: tc2=", tc2);
