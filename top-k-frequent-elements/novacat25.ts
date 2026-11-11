/*
공간 복잡도: O(n)
시간 복잡도: O(n)
풀이: nums의 length만큼 버킷을 생성하여 Bucket Sort 적용 후 빈도가 높은 순서대로 k개의 숫자를 선택한다.
풀이 History
1차: JavaScript Map + Max Heap을 이용해 k개의 숫자를 선택하는 방식으로 구현했다.(O(nlogk) 시간 복잡도) 문제 조건 상 시간 복잡도가 O(nlogn) 이하로 나와야 하므로 2차에서 Bucket Sort를 적용하여 O(n) 시간 복잡도로 구현하였다.
2차: 아래의 코드대로 Bucket Sort를 적용하여 k개의 숫자를 선택하는 방식으로 수정했다.(O(n) 시간 복잡도)
개선점: for 문을 그대로 쓰지 않고, 함수를 만들어서 재사용성을 높이는 방안도 좋을 것으로 생각됨.
*/
const getBucketSort = (freqArr: number[][], n: number) => {
  // freq 값을 그대로 index로 활용하고 싶기 때문에 n+1개의 버킷을 생성한다.(index 0은 사용하지 않음)
  const buckets: number[][] = Array.from({ length: n + 1 }, () => [])

  for (const [num, freq] of freqArr) {
    buckets[freq].push(num)
  }

  return buckets
}

const topKFrequent = (nums: number[], k: number): number[] => {
  const answerArr: number[] = []
  const entryArr: number[][] = []

  const numberMap = new Map<number, number>()

  for (const val of nums) {
    const count = (numberMap.get(val) || 0) + 1
    numberMap.set(val, count)
  }

  for (const entry of numberMap.entries()) {
    entryArr.push(entry)
  }

  const bucketArr = getBucketSort(entryArr, nums.length)

  for (let i = bucketArr.length - 1; i >= 0; i--) {
    for (const num of bucketArr[i]) {
      answerArr.push(num)

      if (answerArr.length === k) {
        return answerArr
      }
    }
  }

  return answerArr
}
