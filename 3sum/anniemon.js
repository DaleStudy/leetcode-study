/**
 * 시간 복잡도:
 *   nums의 길이만큼 for문을 순회하고, 내부에서 투 포인터로 또 한 번 순회하므로, O(n²)
 * 공간 복잡도:
 *   정렬은 추가 공간 사용이 없음.
 *   res 배열의 크기는 고유한 세 숫자 조합의 갯수.
 *   이를 k라고 하면, 공간 복잡도는 O(k)
 */
/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function (nums) {
  nums.sort((a, b) => a - b);
  const res = [];

  for (let i = 0; i < nums.length; i++) {
      if (i > 0 && nums[i] === nums[i - 1]) {
          continue;
      }
      let l = i + 1;
      let r = nums.length - 1;
      while (l < r) {
          const sum = nums[i] + nums[l] + nums[r];
          if (sum > 0) {
              r--;
          } else if (sum < 0) {
              l++;
          } else if (sum === 0) {
              res.push([nums[i], nums[l], nums[r]]);
              l++;
              r--;
              while (l < r && nums[l] === nums[l - 1]) {
                  l++;
              }
          }
      }
  }
  return res;
};
