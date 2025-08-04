// TC: O(n)
// SC: O(1)

function maxArea(height: number[]): number {
  let left = 0;
  let right = height.length - 1;
  let maxWater = 0;

  while (left < right) {
    const x = right - left;
    const y = Math.min(height[left], height[right]);

    maxWater = Math.max(x * y, maxWater);

    if (height[left] <= height[right]) {
      left += 1;
    } else {
      right -= 1;
    }
  }

  return maxWater;
}


// ❌ Time Limit Exceeded!
// TC: O(n^2)

// function maxArea(height: number[]): number {
//   // input: an integer array -> height
//   // output: the maximum amount of water
//   // height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

//   let maxWater = 0;

//   for (let start = 0; start < height.length - 1; start++) {
//     for (let end = start + 1; end < height.length; end++) {
//       const x = end - start;
//       const y = Math.min(height[start], height[end]);
//       maxWater = Math.max(maxWater, x * y);
//     }
//   }

//   return maxWater;
// }
