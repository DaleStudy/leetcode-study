/*
시간 복잡도(Time Complexity): 평균 O(n)
공간 복잡도(Space Complexity): 평균 O(n)
풀이 알고리즘: JavaScript Set 이용

풀이 History
1트: JavaScript Set을 떠올렸으나, for(const val of st) 부분에서 불필요한 부분을 탐색하여 TLE가 터졌다. (X)
2트: [...st]를 이용해 Set을 Array로 변환 후, for(const val of setArr)로 탐색하여 시간 복잡도를 개선했다. (O(n) 시간 복잡도)

기타: Duplicate identifier 'longestConsecutive' 에러가 발생하는 듯하여 novacatLongestConsecutive라는 이름으로 함수를 변경함.
*/

const novacatLongestConsecutive = (nums: number[]): number => {
  const numberSet = new Set<number>()
  let result = 0

  for (const val of nums) {
    numberSet.add(val)
  }

  const setArr = [...numberSet]
  for (const val of setArr) {
    if (!numberSet.has(val - 1)) {
      let cur = val
      let cnt = 0
      while (numberSet.has(cur)) {
        cur++
        cnt++
      }

      result = Math.max(result, cnt)
    }
  }

  return result
}
