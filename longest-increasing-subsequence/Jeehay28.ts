// Time Complexity: O(n * log n)
// Space Complexity: O(n)

function lengthOfLIS(nums: number[]): number {
  const sub: number[] = []; // O(n)

  for (const num of nums) { // O(n)
    // lower bound binary search: find the first index where element >= target
    let left = 0;
    let right = sub.length;
    const target = num;

    while (left < right) { // O(log n)
      let mid = Math.floor((left + right) / 2);
      if (sub[mid] < target) {
        left = mid + 1;
      } else {
        right = mid;
      }
    }

    // if target is greater than all elements in sub
    if (left === sub.length) {
      sub.push(target);
    } else {
      // replace the first element >= target
      sub[left] = target;
    }
  }

  return sub.length;
}

