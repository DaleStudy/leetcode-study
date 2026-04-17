// math의 min을 이용하는 방법
// tc: O(n^4)
// sc: 잘 몰랐는데 모든 요소를 함수 인자로 풀어 콜스택에 올린다 하여 O(n)이 된다고 함..
// (대용량의 배열 시 maximum exceed 에러가 날 수 있음)
const findMin_use_math_min = function (nums) {
  return Math.min(...nums);
};

// 메서드를 사용하지 않은 풀이.
// tc: O(n^6)
// sc: O(1)
const findMin_naive = function (nums) {
  let min = nums[0];

  for (let i = 1; i < nums.length; i++) {
    if (nums[i] <= min) {
      min = nums[i];
      break;
    }
  }

  return min;
};

// 시간복잡도를 문제의 요구사항에 맞도록 줄여본 풀이
// tc: O(n^2*logn)
// sc: O(1)
const findMin = function (nums) {
  let left = 0,
    right = nums.length - 1;

  while (left < right) {
    let mid = Math.floor((left + right) / 2);

    if (nums[mid] > nums[right]) {
      left = mid + 1;
    } else {
      right = mid;
    }
  }

  return nums[left];
};
