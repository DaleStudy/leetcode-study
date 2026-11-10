/* 
  시간 복잡도(Time Complexity): 평균 O(n)
  공간 복잡도(Space Complexity): 평균 O(n)
  풀이 알고리즘: JS의 HashMap / Map 이용

  풀이 History
  1트: 완전 탐색을 이용해 정답은 맞췄으나, Time Complexity가 O(n²)
  2트: HasyMap을 통해 Key - value 플로를 응용하여 O(n)으로 단축 완료
*/

const twoSum = (nums: number[], target: number): number[] => {
  const map: Map<number, number> = new Map()
  const arr = [0, 0]

  for (let i = 0; i < nums.length; i++) {
    const currentNum = nums[i]
    const anotherPair = target - currentNum

    if (map.has(anotherPair)) {
      // map.has로 값을 가지고 있음이 확정되어 있으므로 non-null assertion을 통해 값 강제
      arr[0] = map.get(anotherPair)!
      arr[1] = i

      break
    }

    map.set(currentNum, i)
  }

  return arr
}
