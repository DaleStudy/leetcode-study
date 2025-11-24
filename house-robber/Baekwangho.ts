/** 1차 시도
function rob(nums: number[]): number {
  const jumpArray = []

    if (nums.length<3) {
        nums.sort((a,b)=> b-a)
        return nums[0]
    }

  for (let i = 0; i<=nums.length-3; i++) {
    jumpArray.push(nums[i]+nums[i+2])
  }  

  let maximum = 0

  for (let i = 0; i<jumpArray.length-2; i+=3) {
    if(jumpArray[i] >= jumpArray[i+1]) {
        maximum += jumpArray[i]
    }else{
        maximum += jumpArray[i+1]
    }
  }

  return maximum
};
*/

/** 2차 시도, 풀이 참고
f(nums) => nums 를 털어 구할 수 있는 가장 큰 금액
첫집부터 털었을 때: nums[0] + f(nums[2:])
둘째집부터 털었을 때: f(nums[1:])

첫 시작
f(nums) = MAX(nums[0] + f(nums[2:]), f(nums[1:]))

function rob(nums: number[]): number {
    function f (num: number) {
        if(nums.length - 1 < num) {
            return 0
        }

        const first = nums[num] + f(num + 2)
        const second = f(num + 1)
        return first >= second ? first : second
    }

    return f(0)
}
 */

function rob(nums: number[]): number {
  const resultMap = new Map();

  function f(num: number) {
    if (resultMap.has(num)) {
      return resultMap.get(num);
    }

    if (nums.length - 1 < num) {
      resultMap.set(num, 0);
    } else {
      const first = nums[num] + f(num + 2);
      const second = f(num + 1);

      const result = first >= second ? first : second;
      resultMap.set(num, result);
    }

    return resultMap.get(num);
  }

  return f(0);
}
