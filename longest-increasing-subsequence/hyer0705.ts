// using binary search, lower bound
function lengthOfLIS(nums: number[]): number {
  const n = nums.length;
  const sub: number[] = [];

  for (const num of nums) {
    if (sub.length === 0 || num > sub[sub.length - 1]) {
      sub.push(num);
    } else if (num <= sub[sub.length - 1]) {
      let l = 0;
      let r = sub.length - 1;

      while (l < r) {
        const mid = Math.floor((l + r) / 2);

        if (num <= sub[mid]) {
          r = mid;
        } else {
          l = mid + 1;
        }
      }

      sub[l] = num;
    }
  }

  return sub.length;
}

// using dp
function lengthOfLIS(nums: number[]): number {
  const n = nums.length;
  const dp: number[] = Array(n).fill(1);

  for (let i = 1; i < n; i++) {
    for (let j = 0; j < i; j++) {
      if (nums[j] < nums[i]) {
        dp[i] = Math.max(dp[i], dp[j] + 1);
      }
    }
  }

  return Math.max(...dp);
}
