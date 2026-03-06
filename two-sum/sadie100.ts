/*
풀이
해시맵을 이용해 현재 값의 보수(target - num)가 이미 등장했는지 확인한다.


시간복잡도
O(N) - nums 순회

공간복잡도
O(N) - numObj 생성
*/

function twoSum(nums: number[], target: number): number[] {
  const numObj: { [key: number]: number } = {}

  for (let i = 0; i < nums.length; i++) {
    const num = nums[i]
    if (target - num in numObj) {
      return [i, numObj[target - num]]
    } else {
      numObj[num] = i
    }
  }

  return []
}
