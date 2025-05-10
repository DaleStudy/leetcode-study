// Time: O(n log n), Space: O(n)
function lengthOfLIS(nums) {
    const tails = [];
  
    for (const num of nums) {
      let left = 0, right = tails.length;
      
      // 이진 탐색: tails에서 num이 들어갈 최소 위치 찾기
      while (left < right) {
        const mid = Math.floor((left + right) / 2);
        if (tails[mid] < num) {
          left = mid + 1;
        } else {
          right = mid;
        }
      }
  
      // left는 삽입 위치
      tails[left] = num;
    }
  
    return tails.length;
}
