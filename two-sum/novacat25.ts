/*
  시간 복잡도(Time Complexity): 평균 O(n)
  공간 복잡도(Space Complexity): O(n)
  풀이 알고리즘: JavaScript Map 활용

  풀이 History
  1트: 완전 탐색을 이용해 정답은 맞췄으나,
       시간 복잡도가 O(n²)로 비효율적이었음.

  2트: JavaScript Map을 활용하여
       숫자와 인덱스를 Key-Value 형태로 관리.
       보완해야 할 숫자의 존재 여부를 평균 O(1)에 탐색하여
       전체 시간 복잡도를 O(n)으로 개선.
*/

const twoSum = (nums: number[], target: number): number[] => {
  const numToIndexMap: Map<number, number> = new Map()

  for (let i = 0; i < nums.length; i++) {
    const currentNum = nums[i]
    const complement = target - currentNum

    const complementIndex = numToIndexMap.get(complement)

    if (complementIndex !== undefined) {
      return [complementIndex, i]
    }

    numToIndexMap.set(currentNum, i)
  }

  // Fallback 값으로 임의로 반환하지 않고, 예외를 발생시켜 문제 조건에 맞지 않는 경우를 명시적으로 처리함.
  throw new Error("No valid pair found")
}
