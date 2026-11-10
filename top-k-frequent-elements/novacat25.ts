/*
공간 복잡도: O(n)
시간 복잡도: O(n)
풀이: nums의 length만큼 버킷을 생성하여 Bucket Sort 적용 후 빈도가 높은 순서대로 k개의 숫자를 선택한다.
풀이 History
1차: HashMap + Max Heap을 이용해 k개의 숫자를 선택하는 방식으로 구현하였다.(O(nlogk) 시간 복잡도) 문제 조건 상 시간 복잡도가 O(nlogn) 이하로 나와야 하므로 2차에서 Bucket Sort를 적용하여 O(n) 시간 복잡도로 구현하였다.
2차: 아래의 코드대로 Bucket Sort를 적용하여 k개의 숫자를 선택하는 방식으로 구현하였다.(O(n) 시간 복잡도)
*/
const getBucketSort = (freqArr: number[][], n: number) => {
  const buckets: number[][] = Array.from({ length: n + 1 }, () => [])

  // Put array elements in different buckets
  for (let i = 0; i < freqArr.length; i++) {
    const [num, freq] = freqArr[i]
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
