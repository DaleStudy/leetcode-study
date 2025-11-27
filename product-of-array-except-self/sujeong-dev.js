/**
 * @param {number[]} nums
 * @return {number[]}

 result[i] = (nums[0] * ... * nums[i-1]) * (nums[i+1] * nums[n-1])
 i=0 r[0]= 1
 i=1 r[1]= 1 * nums[0] = 1
 i=2 r[2]= 1 * nums[0] * nums[1] = 2
 i=3 r[3]= 1 * nums[0] * nums[1] * nums[2] = 6

 i=0 r[0]=24
 i=1 r[1]= 1 * nums[3] * nums[2] = 12
 r=2 r[2]= 1 * nums[3] =4
 r=3 r[3]= 1

 i=0 r[0]=1 * 24
 i=1 r[1]=1 * 12
 i=2 r[2]=2 * 4
 i=3 r[3]=6 * 1
 인덱스를 중심으로 왼쪽 구간 원소의 곱 * 오른쪽 구간 원소의 곱

 시간복잡도 계산
 왼쪽 구간 for문 nums에 비례해서 연산
 오른쪽 구간 for문 nums에 비례해서 연산
 => O(n)

 공간복잡도 계산
 start, end 할당(출력공간인 resultArray배열은 추가공간에서 제외된다.)
 => O(1)
 */
var productExceptSelf = function (nums) {
  let resultArray = Array(nums.length).fill(1);
  const n = nums.length;

  let start = 1;
  for (let i = 1; i < n; i++) {
    start *= nums[i - 1];
    resultArray[i] = start;
  }

  let end = 1;
  for (let i = n - 2; i >= 0; i--) {
    end *= nums[i + 1];
    resultArray[i] *= end;
  }

  return resultArray;
};
