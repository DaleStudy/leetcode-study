/**
 *
 * @link https://leetcode.com/problems/longest-increasing-subsequence/description/
 *
 * 접근 방법 : dp 사용
 *  - dp[i]에 i번째 요소 포함한 LIS 길이 저장
 *  - 현재 값이 이전값보다 큰 경우, 이전값 순회하면서 LIS 업데이트하기
 *
 * 시간복잡도 : O(n^2)
 *  - 각 nums 순회하면서 이전값 비교하기 위해 순회하니까 O(n^2)
 *
 * 공간복잡도 : O(n)
 *  - nums 길이만큼 dp 배열 생성하니까 O(n)
 */

function lengthOfLIS(nums: number[]): number {
  const dp = Array(nums.length).fill(1);

  for (let i = 1; i < nums.length; i++) {
    for (let j = 0; j < i; j++) {
      if (nums[j] < nums[i]) dp[i] = Math.max(dp[i], dp[j] + 1);
    }
  }

  return Math.max(...dp);
}

/**
 *
 * 접근 방법 : 이진 탐색 사용
 *  - num 삽입할 인덱스 찾기 위해서 이진 탐색 사용
 *  - nums 배열 순회하면서 각 num의 위치 찾기
 *  - 위치가 배열 내에 존재하면 기존 값을 대체하고, 위치가 배열 길이보다 크면 배열에 추가
 *
 * 시간복잡도 : O(nlogn)
 *  - nums 배열의 각 요소에 대해 이진 탐색 O(nlogn)
 *
 * 공간복잡도 : O(n)
 *  - arr의 최대 크기가 nums 길이만큼 필요
 */

function lengthOfLIS(nums: number[]): number {
  const arr: number[] = [];

  nums.forEach((num) => {
    let left = 0,
      right = arr.length;
    // num 삽입할 위치를 이진 탐색으로 찾음
    while (left < right) {
      const mid = Math.floor((left + right) / 2);

      if (arr[mid] < num) {
        left = mid + 1;
      } else right = mid;
    }

    // 기존 값 대체
    if (left < arr.length) arr[left] = num;
    // 새로운 값 추가
    else arr.push(num);
  });

  return arr.length;
}
