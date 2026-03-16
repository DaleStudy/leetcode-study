// brute force 방식으로 풀이 - O(n^2)
const productExceptSelf = (nums) => {
  const answer = [];
  for (let i = 0; i < nums.length; i++) {
    let product = 1;
    for (let j = 0; j < nums.length; j++) {
      if (i !== j) {
        product *= nums[j];
      }
    }
    answer.push(product);
  }
  return answer;
};

// Prefix-Suffix Array - 시간 O(n) / 공간 O(n)
const productExceptSelf2 = (nums) => {
  const n = nums.length;

  // 1. 세 배열을 만든다
  const prefix = new Array(n).fill(1);
  const suffix = new Array(n).fill(1);
  const answer = new Array(n).fill(1);

  // 2. prefix 채우기: 왼쪽 누적곱
  //    i=0은 왼쪽이 없으므로 그대로 1
  //    i=1부터 시작
  for (let i = 1; i < n; i++) {
    prefix[i] = prefix[i - 1] * nums[i - 1];
  }

  // 3. suffix 채우기: 오른쪽 누적곱
  //    i=n-1은 오른쪽이 없으므로 그대로 1
  //    i=n-2부터 시작
  for (let i = n - 2; i >= 0; i--) {
    suffix[i] = suffix[i + 1] * nums[i + 1];
  }

  // 4. prefix * suffix
  for (let i = 0; i < n; i++) {
    answer[i] = prefix[i] * suffix[i];
  }

  return answer;
};

// Two-Pass Optimized - 시간 O(n) / 공간 O(1)
const productExceptSelf3 = (nums) => {
  const products = new Array(nums.length).fill(1);

  // 1. before로 왼쪽 누적곱을 products[i+1]에 누적
  let before = 1;
  for (let i = 0; i < nums.length - 1; i++) {
    before *= nums[i];
    products[i + 1] *= before;
  }

  // 2. after로 오른쪽 누적곱을 products[i-1]에 누적
  let after = 1;
  for (let i = nums.length - 1; i > 0; i--) {
    after *= nums[i];
    products[i - 1] *= after;
  }

  return products;
};
