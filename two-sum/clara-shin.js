/**
 * 문제 파악:
 * 정수 배열 nums와 목표값 target이 주어졌을 때, 두 숫자를 더해서 target이 되는 두 수의 인덱스를 찾는 문제
 * follow-up: 브루트 포스(이중 반복문 -> O(n^2)) 접근법보다 효율적인 해시맵을 사용하여 해결
 * => 배열을 한 번만 순회하기 때문에 선형 시간 복잡도 O(n)
 *
 * 접근 방식:
 * (1) 숫자와 해당 인덱스를 저장하기 위해 Map 객체 사용
 * (2) 배열을 한 번만 순회하면서 각 요소를 확인하는데,
 * (3) 각 숫자에 대해, target - 현재 숫자가 이미 해시맵에 있는지 확인해서
 * 있다면: 찾은 숫자와 현재 숫자의 인덱스를 반환하고
 * 없다면: 현재 숫자와 그 인덱스를 해시맵에 저장하고 계속 진행
 */

/**
 * @param {number[]} nums - 정수 배열
 * @param {number} target - 목표 합계 값
 * @return {number[]} - 합이 목표값이 되는 두 수의 인덱스
 */
var twoSum = function (nums, target) {
  const numMap = new Map();

  for (let i = 0; i < nums.length; i++) {
    const currentNum = nums[i];

    const complement = target - currentNum;

    if (numMap.has(complement)) {
      return [numMap.get(complement), i];
    }

    numMap.set(currentNum, i);
  }

  return [];
};
