// Time complexity: O(n)
// Space complexity: O(n)

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function (nums) {
  let count0 = 0;

  const totalProduct = nums.reduce((acc, num) => {
    if (num === 0) {
      count0++;
    }

    return acc * num;
  }, 1);

  return nums.map((num) => {
    if (num === 0) {
      // 0이 2 개 이상 존재할 때
      if (count0 > 1) {
        return 0;
      }

      // 0이 1 개 존재할 때
      // 0을 제외한 나머지 product 계산 (이 과정은 단 한번만 존재하기 때문에 시간 복잡도는 여전히 O(n))
      return nums.filter((num) => num !== 0).reduce((a, c) => a * c, 1);
    }

    return totalProduct / num;
  });
};
