/**
문제의 핵심은 '어떻게 인덱스와 곱을 이중 반복문을 쓰지 않고 해결하느냐'다. 'Goal' → 시간 복잡도 : O(N)
여기서 사용된 개념: 'Two Pointer'
Two Pointer? → '배열에서 순차적으로 접근해야 할 때 두 개의 점의 위치를 기록하면서 처리하는 알고리즘'
이중 반복을 사용하지 않고, 각 인덱스를 순회하면서 answer[index]에 본인을 제외한 곱셈을 중첩시킨다.
본인을 제외한 나머지 원소의 곱이기 때문에 left와 right로 나눠서 중첩된 곱셈을 다시 곱한다.
 */

/**
 * @param {number[]} nums
 * @return {number[]}
 */
function productExceptSelf(nums) {
  let answer = new Array(nums.length).fill(1);

  let left = 0;
  let right = nums.length - 1;

  let mul_left = 1;
  let mul_right = 1;

  while (left < nums.length && right >= 0) {
    answer[left] *= mul_left;
    mul_left *= nums[left]; // 자기 자신 제외 곱

    answer[right] *= mul_right;
    mul_right *= nums[right];

    left++;
    right--;
  }

  return answer;
}
