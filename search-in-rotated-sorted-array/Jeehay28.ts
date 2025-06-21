// TC: O(log n)
// SC: O(1)
function search(nums: number[], target: number): number {
  let left = 0;
  let right = nums.length - 1;

  while (left <= right) {
    const mid = Math.floor((left + right) / 2);

    if (nums[mid] === target) return mid;

    if (nums[left] <= nums[mid]) {
      // Left half is sorted
      if (nums[left] <= target && target < nums[mid]) {
        right = mid - 1;
      } else {
        left = mid + 1;
      }
    } else {
      // Right half is sorted
      if (nums[mid] < target && target <= nums[right]) {
        left = mid + 1;
      } else {
        right = mid - 1;
      }
    }
  }

  return -1;
}

// TC: O(log n)
// SC: O(1)
// function search(nums: number[], target: number): number {
//   const findPivot = (nums: number[]) => {
//     let left = 0;
//     let right = nums.length - 1;

//     while (left <= right) {
//       const mid = Math.floor((left + right) / 2);
//       if (mid > 0 && nums[mid - 1] > nums[mid]) return mid;
//       if (nums[0] <= nums[mid]) {
//         left = mid + 1;
//       } else {
//         right = mid - 1;
//       }
//     }
//     return 0;
//   };

//   const binarySearch = (left: number, right: number) => {
//     while (left <= right) {
//       const mid = Math.floor((left + right) / 2);
//       if (nums[mid] === target) return mid;
//       if (nums[mid] < target) {
//         left = mid + 1;
//       } else {
//         right = mid - 1;
//       }
//     }
//     return -1;
//   };

//   const pivot = findPivot(nums);
//   return Math.max(
//     binarySearch(0, pivot - 1),
//     binarySearch(pivot, nums.length - 1)
//   );
// }
