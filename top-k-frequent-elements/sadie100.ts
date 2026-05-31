/**
nums를 순회하며 {[num]: 등장횟수} 형태의 데이터로 바꾸고, 순회가 끝난후
해당 데이터를 등장횟수 기준으로 내림차순 정렬하여 상위 k개를 리턴한다

O(N)
시간복잡도 : O(NlogN)
nums 순회 - O(N), 객체 배열화 - O(N), 정렬 - O(NLogN) 도합 O(NLogN)
 */

function topKFrequent(nums: number[], k: number): number[] {
  const countObj: Record<number, number> = {}

  for (let num of nums) {
    if (num in countObj) {
      countObj[num] += 1
    } else {
      countObj[num] = 1
    }
  }

  const countArr = Object.entries(countObj)
    .sort((a, b) => b[1] - a[1])
    .map(([num, cnt]) => Number(num))
    .filter((val, idx) => idx < k)

  return countArr
}
