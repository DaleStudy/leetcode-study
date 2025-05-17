/** 첫번째 풀이: 재귀
 * 시간복잡도: O(2^n)
 */
/**
 * 
var maxArea = function(height) {
    let maxWater = (height.length - 1) * Math.min(height[0], height[height.length-1]);
    function recursion(start, end){
        if(start >= end){
            // start와 end가 같거나 start가 end보다 커진 경우
            return;
        }
        maxWater = Math.max(maxWater, (end-start)*(Math.min(height[start], height[end])));
        recursion(start+1, end); // 왼쪽 늘려보고
        recursion(start, end-1); // 우측 늘려보기
    }
    recursion(0, height.length-1);
    return maxWater;
};

/**
 * 두번째 풀이: 투포인터
 * 시간 복잡도: O(n)
 */
/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function (height) {
  let left = 0;
  let right = height.length - 1;
  let maxWater = 0;

  while (left < right) {
    // 현재 포인터 위치에서 물의 양 계산
    const water = (right - left) * Math.min(height[left], height[right]);
    maxWater = Math.max(maxWater, water);

    // 더 작은 높이를 가진 쪽의 포인터를 이동
    // 물의 양은 더 작은 높이에 의해 제한되기 때문에 작은 높이를 가리키던 포인터를 이동
    if (height[left] < height[right]) {
      left++;
    } else {
      right--;
    }
  }

  return maxWater;
};
