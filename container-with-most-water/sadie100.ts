/*
시작인덱스 start와 끝인덱스 end를 지정하고 result 변수를 갱신, start와 end를 좁혀가며 최대 result를 찾는다
 - start와 end 중 더 작은 값을 옮겨가며 값을 비교.
 - 둘이 겹쳐지면 리턴한다.

result를 리턴

시간복잡도 : O(N), 공간복잡도 : O(1)
*/

function maxArea(height: number[]): number {
  let start = 0
  let end = height.length - 1
  let result = 0

  function getAmount(startIdx: number, endIdx: number): number {
    return (endIdx - startIdx) * Math.min(height[endIdx], height[startIdx])
  }

  while (start < end) {
    const area = getAmount(start, end)
    result = Math.max(result, area)

    if (height[start] < height[end]) {
      start += 1
    } else {
      end -= 1
    }
  }

  return result
}
