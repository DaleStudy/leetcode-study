function maxArea(height: number[]): number {
  let left = 0;
  let right = height.length - 1;
  let max = -1;

  while (right > left) {
    const v = Math.min(height[left], height[right]) * (right - left);
    max = Math.max(max, v);
    if (height[left] >= height[right]) {
      right--;
    } else {
      left++;
    }
  }
  return max;
}

/*
1. Math.min(height[left], height[right]) * (right - left);
2. left 와 right 를 양 끝에서 가리킴
3. 너비를 계산해서 max 값을 갱신하고, 둘 중 더 짧은 쪽을 안쪽으로 이동
4. left 와 right 가 만나면 종료
 */
