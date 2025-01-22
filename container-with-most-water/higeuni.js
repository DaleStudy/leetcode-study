/**
 * @param {number[]} height
 * @return {number}
 * 
 * complexity
 * time: O(n)
 * space: O(1)
 */

var maxArea = function(height) {
  let answer = 0;
  let l = 0, r = height.length - 1;
  
  while(l < r) {
      const area = (r - l) * Math.min(height[l], height[r]);

      answer = area > answer ? area : answer;
      
      if(height[l] < height[r]) {
          l += 1;
      }else {
          r -= 1;
      }
  }

  return answer;
};

