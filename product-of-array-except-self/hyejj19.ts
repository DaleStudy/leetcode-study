// answer[i] -> nums[i] 제외한 나머지의 곱
function productExceptSelf(nums: number[]): number[] {
  let left = [];
  let right = [];
  let acc = 1;

  for (let i = 0; i < nums.length; i++) {
    left[i] = acc; // 이전결과까지의 누적값을 i번째에 저장
    acc = acc * nums[i]; // 다음 저장을 위해 업데이트
  }

  acc = 1;
  for (let i = nums.length - 1; i >= 0; i--) {
    right[i] = acc;
    acc = acc * nums[i];
  }

  let answer = [];
  for (let i = 0; i < nums.length; i++) {
    answer.push(left[i] * right[i]);
  }

  return answer;
}

// 2번째 시도
// 공간복잡도를 O(1)로 줄일 수 있을까?
// answer[i] -> nums[i] 제외한 나머지의 곱
function productExceptSelf(nums: number[]): number[] {
  let answer = [];
  let acc = 1;

  for (let i = 0; i < nums.length; i++) {
    answer[i] = acc; // 이전결과까지의 누적값을 i번째에 저장
    acc = acc * nums[i]; // 다음 저장을 위해 업데이트
  }

  acc = 1;
  for (let i = nums.length - 1; i >= 0; i--) {
    answer[i] = answer[i] * acc;
    acc = acc * nums[i];
  }

  return answer;
}
