/*
시간 복잡도(TC): O(n)
공간 복잡도(SC): O(1)
풀이: Left Product & Right Product를 구한 후, 두 값을 곱하여 결과값을 도출한다.

풀이 이력
1트: slice()를 이용하여 Left Product & Right Product를 구했으나, 불필요한 배열 생성으로 인해 시간 복잡도가 O(n^2). TLE 발생.
2트: Left Product & Right Product를 구할 때, slice()를 이용하지 않고, 단순 반복문을 통해 값을 곱하여 결과값을 도출. 시간 복잡도 O(n)으로 개선.
*/
const novacatProductExceptSelf = (nums: number[]): number[] => {
  const resultArr = new Array<number>(nums.length).fill(1)

  let leftProductedVal = 1
  let rightProductedVal = 1

  const lastIdx = nums.length - 1

  // Left Product 계산
  for (let i = 1; i <= lastIdx; i++) {
    leftProductedVal *= nums[i - 1]
    resultArr[i] = leftProductedVal
  }

  // Right Product 계산
  for (let i = lastIdx - 1; i >= 0; i--) {
    rightProductedVal *= nums[i + 1]
    resultArr[i] *= rightProductedVal
  }

  return resultArr
}

/* 1트 풀이 코드 */
/*
const productExceptSelf = (nums: number[]): number[] => {
    const resultArr: number[] = Array.from( {length: nums.length}, () => 0)

    for(let i = 0; i < nums.length; i++) {
    const leftNums = nums.slice(0,i)
    const rightNums = nums.slice(i + 1,nums.length)
    let leftResult = 1
    let rightResult = 1

    if(leftNums) {
        for(const num of leftNums) {
        leftResult *= num
        }
    }

    if(rightNums){
        for(const num of rightNums) {
        rightResult *= num
        }
    }

    resultArr[i] = leftResult * rightResult
    }

    return resultArr
}
*/
