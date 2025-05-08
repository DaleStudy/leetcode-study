/**
 * 최장 증가 부분 수열(Longest Increasing Subsequence, LIS)'을 구하기
 * 부분 수열(Subsequence): 원래 수열에서 몇 개의 원소를 골라서 순서를 바꾸지 않고 나열한 것
 * 증가 부분 수열(Increasing Subsequence): 부분 수열의 원소들이 오름차순으로 정렬된 것
 *
 * 접근방법: 동적계획법(DP) 또는 이진탐색(Binary Search)
 * 1. DP를 이용한 방법: 시간복잡도 O(n^2)
 * 2. 이진탐색을 이용한 방법: 시간복잡도 O(n log n) ✅ follow-up 고려
 */

/** 동적계획법(DP)으로 접근
 * @param {number[]} nums
 * @return {number}
 */
var lengthOfLIS = function (nums) {
  if (nums.length === 0) return 0;

  // dp[i]는 인덱스 i까지의 가장 긴 증가 부분 수열의 길이
  const dp = Array(nums.length).fill(1);

  // 모든 위치에 대해 검사
  for (let i = 1; i < nums.length; i++) {
    // 현재 위치보다 이전의 모든 위치를 검사
    for (let j = 0; j < i; j++) {
      // 현재 값이 이전 값보다 크면, 이전 위치의 LIS에 현재 값을 추가할 수 있음
      if (nums[i] > nums[j]) {
        // 기존 값과 (이전 위치의 LIS 길이 + 1) 중 더 큰 값을 선택
        dp[i] = Math.max(dp[i], dp[j] + 1);
      }
    }
  }

  // dp 배열에서 가장 큰 값이 LIS의 길이
  return Math.max(...dp);
};

/** 이진탐색(Binary Search)으로 접근
 * @param {number[]} nums
 * @return {number}
 */
var lengthOfLIS = function (nums) {
  if (nums.length === 0) return 0;

  // tails[i]는 길이가 i+1인 증가 부분 수열의 마지막 원소 중 가장 작은 값
  const tails = [];

  for (let num of nums) {
    // 이진 탐색으로 num이 들어갈 위치 찾기
    let left = 0;
    let right = tails.length;

    while (left < right) {
      const mid = Math.floor((left + right) / 2);
      if (tails[mid] < num) {
        left = mid + 1;
      } else {
        right = mid;
      }
    }

    // 찾은 위치에 num 삽입 또는 대체
    if (left === tails.length) {
      tails.push(num); // 새로운 최장 길이 발견
    } else {
      tails[left] = num; // 기존 값 갱신
    }
  }

  // tails 배열의 길이가 LIS의 길이
  return tails.length;
};
