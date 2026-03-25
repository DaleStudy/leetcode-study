/*
배열을 정렬한 뒤 엘리먼트 하나를 고정하고, 해당 엘리먼트보다 큰 범위에서 투 포인터 순회로 합이 -{엘리먼트값} 이 되는 쌍을 찾는 로직을 모든 배열 엘리먼트에 순회하며 적용한다

시간복잡도 : O(N^2)
=> 엘리먼트 고정 순회 n * 투 포인터 순회 n

공간복잡도 : O(N) 
=> 정렬된 배열
*/

function threeSum(nums: number[]): number[][] {
  const sortedNums = nums.sort((a, b) => a - b)
  const result = []
  let beforeIVal

  for (let i = 0; i < nums.length; i++) {
    const idxVal = sortedNums[i]
    if (beforeIVal !== undefined && beforeIVal === idxVal) {
      continue
    }
    beforeIVal = idxVal
    const shouldBe = -idxVal
    let start = i + 1
    let end = nums.length - 1

    while (start < end) {
      const startVal = sortedNums[start]
      const endVal = sortedNums[end]
      const value = startVal + endVal
      if (value === shouldBe) {
        result.push([idxVal, startVal, endVal])
        start += 1
        end -= 1
        while (startVal === sortedNums[start]) {
          start += 1
        }
        while (endVal === sortedNums[end]) {
          end -= 1
        }
      } else if (value > shouldBe) {
        end -= 1
      } else {
        start += 1
      }
    }
  }

  return result
}
