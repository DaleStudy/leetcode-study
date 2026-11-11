/*
  시간 복잡도(Time Complexity): 평균 O(n)
  공간 복잡도(Space Complexity): O(n)
  풀이 알고리즘: JavaScript Set 활용

  풀이 History
  1트: Array.find()를 이용해 중복 여부를 탐색했으나,
       반복적인 배열 탐색으로 인해 시간 초과(TLE) 발생.

  2트: 배열 정렬 후 Binary Search를 활용하는 방법을 고려했으나,
       정렬에 필요한 추가적인 시간 비용으로 비효율적이라고 판단.

  3트: Set 자료구조를 이용한 풀이로 변경.
       Set.has()를 통해 기존 데이터의 존재 여부를 평균 O(1)에 확인하고,
       Set.add()를 통해 방문한 숫자를 기록.
*/

const containsDuplicate = (nums: number[]): boolean => {
  const set = new Set()

  for (let i = 0; i < nums.length; i++) {
    const currentNum = nums[i]
    if (set.has(currentNum)) {
      return true
    }

    set.add(currentNum)
  }

  return false
}
