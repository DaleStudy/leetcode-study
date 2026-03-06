/*
풀이
nums를 값과 index가 있는 객체 배열 newNums로 재정의한다
newNums를 값 오름차순으로 정렬하고 두 포인터 start, end를 둔다
nums[start] + nums[end]가 target보다 작으면 start+1하고, target보다 크면 end-1한다. 같으면 nums[start]과 nums[end]의 오리진 index를 리턴한다.
만약 start>=end가 되면 빈 배열을 리턴한다

시간복잡도
O(nLogN) - 정렬. 포인터 순회는 O(N)이므로 최종적으로 O(nLogN)

공간복잡도
O(N) : newNums 배열
*/

function twoSum(nums: number[], target: number): number[] {
  const newNums = nums.map((value, idx) => ({ value, idx }))
  const sortedNums = newNums.sort((a, b) => a.value - b.value)
  let start = 0
  let end = nums.length - 1

  while (start < end) {
    const total = sortedNums[start].value + sortedNums[end].value
    if (total === target) {
      return [sortedNums[start].idx, sortedNums[end].idx]
    } else if (total > target) {
      end -= 1
    } else {
      start += 1
    }
  }

  return []
}
