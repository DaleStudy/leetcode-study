// 1번 풀이
function productExceptSelf1(nums: number[]): number[] {
  const result: number[] = new Array(nums.length).fill(1);

  applyLeftProducts(nums, result);
  applyRightProducts(nums, result);

  return result;
};

function applyLeftProducts(nums: number[], result: number[]) {
  let prefix = 1;
  for (let i = 0; i < nums.length; i++) {
    result[i] = prefix;
    prefix *= nums[i];
  }
};

function applyRightProducts(nums: number[], result: number[]) {
  let suffix = 1;
  for (let i = nums.length - 1; i >= 0; i--) {
    result[i] *= suffix;
    suffix *= nums[i];
  }
};

// 2번 풀이
function productExceptSelf2(nums: number[]): number[] {
    const length = nums.length;
    const result: number[] = new Array(length).fill(1);
  
    // 1단계: 왼쪽 누적 곱 저장
    let prefix = 1;
    for (let i = 0; i < length; i++) {
      result[i] = prefix;
      prefix *= nums[i];
    }
  
    // 2단계: 오른쪽 누적 곱 곱하기 (in-place)
    let suffix = 1;
    for (let i = length - 1; i >= 0; i--) {
      result[i] *= suffix;
      suffix *= nums[i];
    }
  
    return result;
  }
  