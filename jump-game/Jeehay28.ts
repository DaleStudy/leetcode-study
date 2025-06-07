// TC: O(n)
// SC: O(1)
function canJump(nums: number[]): boolean {
  //   nums = [3, 2, 1, 0, 4]
  // farthest  3, 3, 3, 3
  let farthest = 0;

  for (let i = 0; i < nums.length; i++) {
    if (i > farthest) return false;
    farthest = Math.max(farthest, nums[i] + i);
  }
  return true;
}


// ❌ TC: O(n^2)
// SC: O(n)

// function canJump(nums: number[]): boolean {
//   const lastIndex = nums.length - 1;
//   const visited = new Map<number, boolean>();

//   const canReach = (current: number): boolean => {
//     if (current === lastIndex) return true;

//     if (visited.has(current)) return visited.get(current) as boolean;

//     for (let i = 1; i <= nums[current]; i++) {
//       if (current + i <= lastIndex) {
//         if (canReach(current + i)) return true;
//       }
//     }

//     visited.set(current, false);

//     return false;
//   };

//   return canReach(0);
// }
