/* 
  시간 복잡도(Time Complexity): 평균 O(n)
  공간 복잡도(Space Complexity): 평균 O(n)
  풀이 알고리즘: JS의 HashMap / Map 이용

  풀이 History
  1트: 예전에 JS의 find() 메서드를 이용해 풀었을 때에는 TLE에 걸리기 일쑤였으니, JS 배열을 정렬(Quick Sort)하고 Binary Search로 일관된 정렬 시간을 확보하자!(X) -> 비효율적인 정렬 코스트로 TLE가 발생하여 틀렸다.
  2트: 이 문제에 정렬(sort) 과정이 필요한가? -> X. 따라서 탐색에 훨씬 유리한 자료구조를 찾아서 푸는 게 낫다고 판단함.
  3트: Map/HashMap을 이용해 Key 기반의 빠른 탐색 및 저장으로 풀자
*/

const containsDuplicate = (nums: number[]): boolean => {
  const set = new Set()

  for (let i = 0; i < nums.length; i++) {
    const currentNum = nums[i]
    if (set.has(currentNum)) {
      return true
    } else {
      set.add(currentNum)
    }
  }

  return false
}
