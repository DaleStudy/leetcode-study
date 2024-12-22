/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function (nums) {
  const result = []; // 결과값
  nums.sort((a, b) => a - b); // 오름차순 정렳

  // 배열 순차 탐색
  for (let i = 0; i < nums.length - 2; i++) {
    // 중복 값 건너뜀
    if (i > 0 && nums[i] === nums[i - 1]) continue;

    let low = i + 1,
      high = nums.length - 1;

    // low와 high 포인터 이용해 합이 0인 값 찾기
    while (low < high) {
      const sum = nums[i] + nums[low] + nums[high];
      if (sum < 0) low++;
      else if (sum > 0) high--;
      else {
        result.push([nums[i], nums[low], nums[high]]);
        // 중복된 값 건너뛰기
        while (low < high && nums[low] === nums[low + 1]) low++;
        while (low < high && nums[high] === nums[high - 1]) high--;
        low++;
        high--;
      }
    }
  }

  return result;
};

// 1시간 정도 문제 풀이를 하다가 정렬까지 한 다음 그 이후 어떻게 해야할지 몰라 풀이 참고
// 문제 풀이에서 핵심은 정렬을 한 다음 두 개의 포인터를 지정해 sum이 0인 값을 찾는 것
// 시간 복잡도: O(n^2) 배열 순차 탐색
// 공간 복잡도: O(1) 결과값 result
