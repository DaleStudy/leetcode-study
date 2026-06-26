/**
문제에서 중요한 것은 '비교를 어디서 어떻게 두나'였다.
[0]번 인덱스에서 시작하거나 [1]번에서 시작하는 두 가지 방식이 있다.
[0]번과 [1]번 각각의 케이스에서 누적된 합을 저장하고 비교한다.
이 값들은 전부 arr 배열의 인덱스에 저장된다.
배열의 원소들이 갖는 의미는 원본 배열 nums의 원소들과 arr 배열의 누적된 값의 합 중 큰 값이다.
이렇게 설계한 경우에 마지막 인덱스 or 마지막 인덱스 -1의 값 중 큰 수인 max number가 반환된다.
 */

/**
 * @param {number[]} nums
 * @return {number}
 */

function rob(nums) {
  switch (nums.length) {
    case 0:
      return 0;
    case 1:
      return nums[0];
    case 2:
      return Math.max(nums[0], nums[1]);
  }

  let arr = [];
  arr[0] = nums[0];
  arr[1] = nums[1];
  arr[2] = nums[0] + nums[2];

  for (let i = 3; i < nums.length; i++) {
    arr[i] = nums[i] + Math.max(arr[i - 2], arr[i - 3]);
  }

  return Math.max(arr[arr.length - 1], arr[arr.length - 2]);
}
