function maxArea(height: number[]): number {
  const n = height.length;

  let maximumArea = 0;
  let l = 0;
  let r = n - 1;

  while (l < r) {
    const currentArea = (r - l) * Math.min(height[l], height[r]);

    maximumArea = Math.max(maximumArea, currentArea);

    if (height[l] > height[r]) {
      r--;
    } else {
      l++;
    }
  }

  return maximumArea;
}
