// 1번째 풀이
function maxArea1(height: number[]): number {
let left = 0;
let right = height.length - 1;
const area: number[] = [];
    
  while (left < right) {
    const x = right - left;
    const y = Math.min(height[left], height[right]);
    area.push(x * y);

    if (height[left] < height[right]) {
      left++;
    } else {
      right--;
    }
  }

  return Math.max(...area);
};

// 2번째 풀이
function maxArea2(height: number[]): number {
  let left = 0;
  let right = height.length - 1;
  let max = 0;

  while (left < right) {
    const x = right - left;
    const y = Math.min(height[left], height[right]);
    const current = x * y;
    max = Math.max(max, current);

    if (height[left] < height[right]) {
      left++;
    } else {
      right--;
    }
  }

  return max;
};
