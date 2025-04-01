/*
  시간복잡도: O(n) - 배열을 두 번 순회하지만 여전히 선형
  배열에서 0의 개수에 따라 결과가 달라지는 점을 이용
  - 0이 두 개 이상: 모든 결과는 0
  - 0이 하나: 0 위치만 전체곱, 나머지는 0
  - 0이 없음: 전체곱 ÷ 현재 원소
*/

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function (nums) {
  // 0이 있는 위치들 체크용
  const zeros = new Map();

  // 전체 곱 구하기 - O(n)
  const allProductExceptZero = nums.reduce((acc, x, i) => {
    if (x === 0) zeros.set(i, true);
    return x !== 0 ? acc * x : acc;
  }, 1);

  // 배열 전체 돌면서 조건에 맞게 return 시키기 - O(n)
  return nums.map((x, i) => {
    // 0이 2개 이상이라면 무조건 0
    if (zeros.size > 1) {
      return 0;
    }

    // 0이 1개일 때
    if (zeros.size === 1) {
      // 그게 나일 때
      if (zeros.has(i)) return allProductExceptZero;

      // 그게 다른애일 때
      return 0;
    }

    // 0이 없을 때
    return allProductExceptZero / x;
  });
};
