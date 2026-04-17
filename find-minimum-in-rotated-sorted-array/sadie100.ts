/**
이분탐색으로 정렬 탐색. 최소값이 들어있는 범위를 바탕으로 계속 좁혀 간다
중간값을 기준값으로 잡고, 마지막 값보다 큰지 작은지 확인한다
  기준값이 마지막 값보다 작을 경우, 최소값은 왼쪽 반쪽에 있거나 기준값임. ex) 5 1 2 3 4
  -> range를 왼쪽 반쪽으로 줄이고(기준값 포함) 해당 중간값을 기준값으로 잡는다
  기준값이 마지막 값보다 클 경우, 최소값은 오른쪽 반쪽에 있음. ex) 3 4 5 1 2
  -> range를 오른쪽 반쪽으로 줄이고 해당 중간값을 기준값으로 잡는다
  
최종적으로 start, end가 같아지는 값이 최소값이 된다.

시간복잡도 : O(LogN) -> N은 nums의 개수. 이분탐색
 */

function findMin(nums: number[]): number {
  let start = 0
  let end = nums.length - 1

  while (start < end) {
    let target = Math.floor((start + end) / 2)
    if (nums[target] < nums[end]) {
      end = target
    } else {
      start = target + 1
    }
  }

  return nums[start]
}
